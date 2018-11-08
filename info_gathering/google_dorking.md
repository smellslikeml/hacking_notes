# Google Dorking (Hacking) Cheatsheet

Check out more: 

* https://itblogsec.com/google-hacking-dorking-tutorial-1/

* https://www.techworm.net/2017/10/google-dorking-use-google-hacking-websites-iot-devices-cameras-etc.html

## Examples


* Wildcards: 'Thomas * Edison' -- expands to Thomas A. Edison, Thomas Alva Edison, etc.

* Synonyms: '~neuroscience' -- expands for synonyms like: neurobiology, brain, etc.

* Range Search: '$100...$500 laptops' -- expands for range of [100, 500]

* allintext: 'allintext:microsoft help email fraud' -- restricts to results with all query terms
  -- allinurl, allintitle

* filetype: 'filetype:pdf' -- return results in the pdf format

* phonebook: 'phonebook:Mr Fox' -- return phonebook query listings

* stocks: 'stocks:msft' -- return stock prices for query entity

## Combining operators:

* intext:@gmail.com filetype:xls -- returns excel files containing @gmail.com... likely a list of contacts
