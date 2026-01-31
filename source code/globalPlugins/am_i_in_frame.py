# -*- coding: UTF-8 -*-
# 我在頁框裡嗎插件
# 按下快捷鍵可朗讀當前焦點是否在頁框（iframe/frame）中

import globalPluginHandler
import api
import ui
import logHandler
import os
import gettext
import languageHandler
from controlTypes import Role

# 初始化翻譯
def internal_init_translation():
    # 初始化插件的國際化翻譯
    try:
        # 獲取插件目錄和 locale 資料夾路徑
        addon_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(addon_dir)
        locale_dir = os.path.join(parent_dir, "locale")

        # 獲取當前 NVDA 使用的語言
        lang = languageHandler.getLanguage()

        # 構建語言回退列表
        languages = [lang]

        # 如果語言代碼包含下劃線，也嘗試主要語言代碼
        if '_' in lang:
            main_lang = lang.split('_')[0]
            languages.append(main_lang)

        # 添加英文作為最終回退
        if 'en' not in languages:
            languages.append('en')

        # 創建翻譯對象
        translation = gettext.translation(
            "nvda",
            localedir=locale_dir,
            languages=languages,
            fallback=True
        )

        return translation.gettext

    except Exception:
        # 如果初始化失敗，返回原文
        return lambda x: x

# 獲取翻譯函數
_ = internal_init_translation()

# 頁框相關的角色類型
FRAME_ROLES = {
    Role.INTERNALFRAME,  # iframe
    Role.FRAME,          # frame
}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # 我在頁框裡嗎插件

    # Translators: 輸入手勢類別名稱
    scriptCategory = _("Am I In Frame")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logHandler.log.info("Am I In Frame addon started")

    def terminate(self):
        logHandler.log.info("Am I In Frame addon terminated")

    # 檢查是否在頁框中
    def internal_find_frame(
        self,
        obj  # 起始物件，類型：NVDAObject
    ):
        # 向上遍歷父物件鏈，尋找頁框
        # 返回：(是否在頁框中, 頁框名稱, 頁框層級數)
        frame_count = 0
        frame_names = []

        current = obj
        while current:
            try:
                if current.role in FRAME_ROLES:
                    frame_count += 1
                    if current.name:
                        frame_names.append(current.name)
                current = current.parent
            except Exception:
                break

        return frame_count > 0, frame_names, frame_count

    def script_checkIfInFrame(self, gesture):
        # 檢查當前焦點是否在頁框中
        try:
            obj = api.getFocusObject()

            if not obj:
                # Translators: 無法獲取焦點物件時的提示
                ui.message(_("Cannot get focus object"))
                return

            in_frame, frame_names, frame_count = self.internal_find_frame(obj)

            if in_frame:
                if frame_count == 1:
                    if frame_names:
                        # Translators: 在單個頁框中，有名稱
                        # {name} 會被替換為頁框名稱
                        ui.message(_("In frame: {name}").format(name=frame_names[0]))
                    else:
                        # Translators: 在單個頁框中，無名稱
                        ui.message(_("In frame"))
                else:
                    # 多層巢狀頁框
                    if frame_names:
                        # Translators: 在多層巢狀頁框中，有名稱
                        # {count} 會被替換為頁框層數，{names} 會被替換為頁框名稱列表
                        ui.message(_("In {count} nested frames: {names}").format(
                            count=frame_count,
                            names=", ".join(frame_names)
                        ))
                    else:
                        # Translators: 在多層巢狀頁框中，無名稱
                        # {count} 會被替換為頁框層數
                        ui.message(_("In {count} nested frames").format(count=frame_count))
            else:
                # Translators: 不在頁框中
                ui.message(_("Not in frame"))

        except Exception as e:
            logHandler.log.error(f"Error checking frame: {str(e)}")
            # Translators: 檢查發生錯誤時的提示
            ui.message(_("Error checking frame status"))

    # Translators: 檢查是否在頁框中的腳本說明
    script_checkIfInFrame.__doc__ = _("Check if current focus is inside a frame")

    # 快捷鍵綁定
    __gestures = {
        "kb:NVDA+shift+m": "checkIfInFrame"
    }
