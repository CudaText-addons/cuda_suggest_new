MAX_LINES = 10
BADS = ' \t?\'"/\\`*<>'

def mask_chars(s, chars):

    for ch in chars:
        s = s.replace(ch, '_')
    return s

class Command:
    
    def on_save_naming(self, ed_self):
        
        cnt = ed_self.get_line_count()
        for i in range(min(MAX_LINES, cnt)):
            line = ed_self.get_text_line(i).strip()
            if line:
                return mask_chars(line, BADS)
