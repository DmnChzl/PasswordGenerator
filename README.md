![Image](https://raw.githubusercontent.com/MrDoomy/PasswordGenerator/master/dev/images/password_generator.png)

This is a simple script to generate classic or custom password.

This includes features like :
- Generate classic password
- Generate custom password
- Specify the length of the password
- Specify a pattern for the password
- Return the password in a text file

# Prerequisites

You need to have a Python environment on your computer.

# Usage

You can specify a pattern for your custom password with `--pattern=[value]`. For example, if you want to create password of twelve characters with four numbers in the beginning and eigth uppercase letters at the end, you can do this like that : `--pattern='{N4}{L8}'`, or by specifying length, like this :  `--length=12 --pattern='{N4}{L+}'`. As you wish !

Here is the list of parameters of the pattern : 
- **{L+}** : uppercase letters up to the specified length (by default the length is randomly between eight and sixteen)
- **{c4}** : four lowercase consonants
- **{v6}** : six lowercase vowels
- **{S5}** : five symbols (**{s5}** is the same)
- **{N3}** : three numbers (**{n3}** is the same)
- **{w9}** : nine lowercase letters like a word (for example, `ikifekiza`)

# Screenshot

![Image](https://raw.githubusercontent.com/MrDoomy/MusicCropper/master/dev/screenshots/computer.png)

# License

    Copyright (C) 2016 Damien Chazoule

    This program is free software : you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY ; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
