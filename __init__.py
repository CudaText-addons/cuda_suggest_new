from cudatext import *

MAX_LINES = 10
BADS = ' \t?\'"/\\`*<>'
REASON_API = app_api_version()>='1.0.438'

def mask_chars(s, chars):

    for ch in chars:
        s = s.replace(ch, '_')
    return s

class Command:
    
    def on_save_naming(self, ed_self):

        return self.get_title(ed_self)

    def get_title(self, ed_self):

        cnt = ed_self.get_line_count()
        for i in range(min(MAX_LINES, cnt)):
            line = ed_self.get_text_line(i).strip()
            if line:
                return mask_chars(line, BADS)

    def on_change_slow(self, ed_self):

        if not ed_self.get_filename():
            if REASON_API:
                if ed_self.get_prop(PROP_TAB_TITLE_REASON, '') in ('s', 'p'):
                    return
            ed_self.set_prop(PROP_TAB_TITLE, self.get_title(ed_self))
            if REASON_API:
                ed_self.set_prop(PROP_TAB_TITLE_REASON, 'u')

    def on_open(self, ed_self):

        self.on_change_slow(ed_self)

    def on_save(self, ed_self):

        ed_self.set_prop(PROP_TAB_TITLE, '')
