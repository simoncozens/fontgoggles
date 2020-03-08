import pytest
from fontgoggles.misc.textInfo import TextInfo


testData = [
    ("abc", True, 0, "L", "left", [('abc', 'Latn', 0, 0)]),
    ("\u062D\u062A\u0649", True, 1, "R", "right", [('\u062D\u062A\u0649', 'Arab', 1, 0)]),
    ("\u062D\u062A\u0649123", True, 1, "R", "right", [('\u062D\u062A\u0649', 'Arab', 1, 0), ('123', 'Arab', 2, 3)]),
    ("\u062D\u062A\u0649123", False, 1, "R", "right", [('\u062D\u062A\u0649123', None, None, 0)]),
    ("abc\u062D\u062A\u0649", True, 0, "L", "left", [('abc', 'Latn', 0, 0), ('\u062D\u062A\u0649', 'Arab', 1, 3)]),
    ("\u062D\u062A\u0649abc", True, 1, "R", "right", [('\u062D\u062A\u0649', 'Arab', 1, 0), ('abc', 'Latn', 2, 3)]),
]


@pytest.mark.parametrize("text,shouldApplyBiDi,baseLevel,baseDirection,alignment,segments", testData)
def test_textInfo(text, shouldApplyBiDi, baseLevel, baseDirection, alignment, segments):
    ti = TextInfo(text)
    ti.shouldApplyBiDi = shouldApplyBiDi
    assert baseLevel == ti.baseLevel
    assert baseDirection == ti.baseDirection
    assert alignment == ti.suggestedAlignment
    assert segments == ti.segments
