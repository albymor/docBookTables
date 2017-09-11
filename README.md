# docBookTables

*A tool to create tables in docBook*

## Requirements
Python 2.7


## Usage
Typing `python docBookTables.py -h` in the terminal should result in this output
```
python docBookTables.py -h
usage: docBookTables.py [-h] -r ROWS -c COLS [-f FILENAME] [-o] [-v]

Create docBook table.

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        name of output file
  -o, --output          get the output file
  -v, --verbose         print out the table

mandatory arguments:
  -r ROWS, --rows ROWS  number of rows
  -c COLS, --cols COLS  number of columns
```

For example calling with argv `python docBookTables.py -r 2 -c 3 -v` it gives:
```
<?xml version="1.0" ?>
<table xml:id="XML ID HERE">
  <!--Insert xml:id here-->
  <title>TITLE HERE</title>

  <tgroup cols="3">
    <colspec colwidth="25*"/>
    <colspec colwidth="25*"/>
    <colspec colwidth="25*"/>
    <thead>
      <row>
        <entry align="center">COLUMN HEAD HERE</entry>
        <entry align="center">COLUMN HEAD HERE</entry>
        <entry align="center">COLUMN HEAD HERE</entry>
      </row>
    </thead>
    <tbody>
      <row>
        <!--Row 1-->
        <entry>
          <para>TEXT HERE</para>
        </entry>
        <entry>
          <para>TEXT HERE</para>
        </entry>
        <entry>
          <para>TEXT HERE</para>
        </entry>
      </row>
      <row>
        <!--Row 2-->
        <entry>
          <para>TEXT HERE</para>
        </entry>
        <entry>
          <para>TEXT HERE</para>
        </entry>
        <entry>
          <para>TEXT HERE</para>
        </entry>
      </row>
    </tbody>
  </tgroup>
</table>
```

Adding `-o` args the table is saved in a file called `Table.xml`, or if you want a custom filename just add `-f` followed by the name.

## License
[Apache License](http://www.apache.org/licenses/LICENSE-2.0) Version 2.0, January 2004
