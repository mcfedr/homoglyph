<?php
class Homoglyph
{
    private $chars = '[[chars_list]]';

    private $replacements = [[chars_array]];
    
    public function match($a) {
        return isset($this->replacements[$a]) ? $this->replacements[$a] : null;
    }
}

$a = new Homoglyph();

echo $a->match('С');
echo $a->match('A');
