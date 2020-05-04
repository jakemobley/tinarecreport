# Python CSV/XLS Report Formatter/Aggregator
Fun project to automate tedious data workflows.

A friend in financial services spent an hour each week producing master reconcilliation reports by manually aggregating and reformatting a number of account summaries. At their request, I wrote this script to make the process instantaneous.

It is a rather specific workflow but can be very easily modified for similar purposes. I have used this as a template to speed up development for several projects.

The script is over-commented and variables explicitly named to make customization a breeze.

## GETTING STARTED

This assumes you have python3 and pandas already installed on your machine. If using excel data, you will also need to install the openpyxl library.

```
pip install openpyxl
```

### Clone repository to desired location
```
git clone https://github.com/jakemobley/tinarecreport.git
```

### Add desired reports to directory

Dump individual csv/xls files to be formatted/aggregated into directory containing the .py script. 

### Run correct script for your filetype

Run the appropriate python script for your filetype

CSV

```
	python run tina_report_csv.py
```

Excel

```
	python run tina_report_excel.py
```

## CUSTOMIZE / ADDITIONAL

The script has been overcommented and variables explicitly named so that you may easily modify the script for your purposes.

## FAQ / CONTACT / TROUBLESHOOT

Contact me with questions at jakemobley[at]gmail[dot]com and I will answer as best I can.