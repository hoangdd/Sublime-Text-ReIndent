ReIndent
===

Quickly switch indent by tab and space.
It basically performs:

Indent by tab
 - `View > Indentation > Convert Indentation to Tabs`
 - `View > Indentation > Tab width: 4`

Indent by space
 - `View > Indentation > Tab width: 2`
 - `View > Indentation > Convert Indentation to Spaces`


Install
===
 - Install [PackageControl](https://packagecontrol.io/)
 - Run `Package Control: Add Repository` add [Sublime-Text-ReIndent repository](https://github.com/hoangdd/Sublime-Text-ReIndent.git)
 - Install `Sublime-Text-Reindent` package
 - Restart SublimeText

Usage
===

Open command pallete and type: "Reindent".
Two options will appear:
 - `ReIndent: from tab 4 to space 2`
 - `ReIndent: from space 2 to tab 4`

Or config short key
 - `{ "keys": ["short_key_here"], "command": "re_indent_to_space_two" }`
 - `{ "keys": ["short_key_here"], "command": "re_indent_to_tab_four" }`

---

