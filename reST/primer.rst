reStructuredText Primer
-----------------------
basic syntax and concepts about reST.

Paragraphs

    Use as blocks. seperated by blank line(s), align with indentation.

Inline markup
    *italics*
    **bold**
    ``code``
    \escape

List and Quote-like blocks
    * one
    * two

        1. one
        2. two

            #. one
            #. two

    term
        definition

        continue definition

Source Code

::
    $ pip install pipenv

or::
    set shiftwidth=4

Tables
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

Hyperlinks
`external link <http://www.sphinx-doc.org/en/stable/rest.html>`_

Sections

- # with overline, for parts
- * with overline, for chapters
- =, for sections
- -, for subsections
- ^, for subsubsections
- ", for paragraphs

And use like this:

Python Style Guide
==================


