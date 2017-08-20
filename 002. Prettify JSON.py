'''
Problem:

"{"id": "0001",	"type": "donut","name": "Cake","ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}"

output:

{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" }
		]
}

'''



TAB_SIZE = 4
def prettyJson(s):
  pretty = ''
  buffer = ''
  indent = 0

  for i in range(len(s)):
    c = s[i]
    if c == ' ':
      continue
    elif c in ('{', '['):
      indent += TAB_SIZE
      maybe_prefix = buffer + '\n' if buffer != len(buffer) * ' ' else ''
      pretty += (maybe_prefix + indent * ' ' + c + '\n')
      indent += TAB_SIZE
      buffer = indent * ' '
    elif c in ('}', ']'):
      indent -= TAB_SIZE
      maybe_prefix = buffer + '\n' if buffer != len(buffer) * ' ' else ''
      maybe_comma = ',' if (i + 1 < len(s) and s[i + 1] == ',') else ''
      pretty += (maybe_prefix + indent * ' ' + c + maybe_comma + '\n')
      indent -= TAB_SIZE
      buffer = indent * ' '
    elif c == ',':
      if s[i - 1] in ('}', ']'):
        continue  # Already handled by elif block above.
      pretty += (buffer + c + '\n')
      buffer = indent * ' '
    elif c == ':':
      buffer += (c + ' ')
    else:
      buffer += c

  return pretty[2:]  # Skip first 2 chars, which are always newlines.

s = """
{"id": "0001", "type":      "donut","name": "Cake","ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}"
"""
t = '{ "a": 100 }'
print prettyJson(s)
