from output_builder import OutputBuilder

class OutputPHP(OutputBuilder):
    def __init__(self, file_name, output_dir, template_dir):
        self.file_name = file_name
        OutputBuilder.__init__(self, output_dir, template_dir)

    def _make_map_for_required_chars(self, chars, char_manager):
        m = {}
        for char in chars:
            s = char_manager.get_set_for_char(char)
            m[char] = list(filter(lambda c : c != char, s))
        return m

    def _make_array_string(self, m):
        obj = []
        for k in sorted(m):
            for x in m[k]:
                obj.append('\'' + x + '\' => \'' + k + '\'')
        return 'array(\n        ' + ',\n        '.join(obj) + '\n    )'

    def create(self, char_manager, chars):
        m = self._make_map_for_required_chars(chars, char_manager)
        array_str = self._make_array_string(m)

        text = self._get_template_text().replace('[[chars_list]]', chars).replace('[[chars_array]]', array_str)

        self._write_output(text)
