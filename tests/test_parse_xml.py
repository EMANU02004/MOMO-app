import os, textwrap, tempfile
from etl.parse_xml import parse_sms_records


def test_parse_returns_records():
    xml = textwrap.dedent("""\
        <?xml version="1.0"?>
        <smses>
          <sms address="250780000000" date="1700000000000" body="You have received 5,000 RWF" />
        </smses>
    """)
    with tempfile.NamedTemporaryFile(suffix=".xml", delete=False, mode="w") as f:
        f.write(xml)
        path = f.name
    records = parse_sms_records(path)
    os.unlink(path)
    assert len(records) == 1
    assert records[0]["address"] == "250780000000"
