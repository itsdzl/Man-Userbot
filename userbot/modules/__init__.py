# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from userbot import LOAD, LOGS, NO_LOAD


def __list_all_modules():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(
                any(mod == module_name for module_name in all_modules)
                for mod in to_load
            ):
                LOGS.error("Nama Modules yang anda masukan salah.")
                sys.exit(1)
        else:
            to_load = all_modules
        if NO_LOAD:
            LOGS.info("Modules No Load : {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]
        return to_load
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Modules To Load : %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]

def vc_asst(dec, **kwargs):
    def ult(func):
        kwargs["func"] = (
            lambda e: not e.is_private and not e.via_bot_id and not e.fwd_from
        )
        handler = udB.get_key("VC_HNDLR") or HNDLR
        kwargs["pattern"] = re.compile(f"\\{handler}" + dec)
        vc_auth = kwargs.get("vc_auth", True)
        key = udB.get_key("VC_AUTH_GROUPS") or {}
        if "vc_auth" in kwargs:
            del kwargs["vc_auth"]

        async def vc_handler(e):
            VCAUTH = list(key.keys())
            if not (
                (e.out)
                or (e.sender_id in VC_AUTHS())
                or (vc_auth and e.chat_id in VCAUTH)
            ):
                return
            elif vc_auth and key.get(e.chat_id):
                cha, adm = key.get(e.chat_id), key[e.chat_id]["admins"]
                if adm and not (await admin_check(e)):
                    return
            try:
                await func(e)
            except Exception:
                LOGS.exception(Exception)
                await asst.send_message(
                    LOG_CHANNEL,
                    f"VC Error - <code>{UltVer}</code>\n\n<code>{e.text}</code>\n\n<code>{format_exc()}</code>",
                    parse_mode="html",
                )

        vcClient.add_event_handler(
            vc_handler,
            events.NewMessage(**kwargs),
        )

    return ult

async def vc_joiner(self):
        chat_id = self._chat
        done, err = await self.startCall()

        if done:
            await vcClient.send_message(
                self._current_chat,
                "• Joined VC in <code>{}</code>".format(chat_id),
                parse_mode="html",
            )
            return True
        await vcClient.send_message(
            self._current_chat,
            f"<strong>ERROR while Joining Vc -</strong> <code>{chat_id}</code> :\n<code>{err}</code>",
            parse_mode="html",
        )
        return False

class Player:
    def __init__(self, chat, event=None, video=False):
        self._chat = chat
        self._current_chat = event.chat_id if event else LOG_CHANNEL
        self._video = video
        if CLIENTS.get(chat):
            self.group_call = CLIENTS[chat]
        else:
            _client = GroupCallFactory(
                vcClient, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                path_to_log_file="VCBot.log"
            )
            self.group_call = _client.get_group_call()
            CLIENTS.update({chat: self.group_call})

    async def make_vc_active(self):
        try:
            await vcClient(
                functions.phone.CreateGroupCallRequest(
                    self._chat, title="🎧 Ultroid Music 🎶"
                )
            )
        except Exception as e:
            LOGS.exception(e)
            return False, e
        return True, None
