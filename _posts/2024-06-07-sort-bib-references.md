---
layout: post
title: Sort the references in bib file in TeXstudio
---

If you are willing to sort the references in `.bib` file according to the `article type` and `reference name` in alphabetical order, this article is helpful.

## Steps
The steps for the settings includes:

- A script in Python to read the `.bib` file and order them.
- Setting of `Macro` in TexStudio to run the script.

### Python Script

1. [Click]({{ site.baseurl }}/assets/scripts/sortBib.py) to download the python script to sort the `.bib`.
2. Run the script in cmd
```shell
$ python sortBib bibfilename.bib
```

### Setting of Macro in TeXstudio
1. Click on the `Edit Macros`
2. Select the `Script` option
3. Type in the Macro name
4. Type in the following script in textbox
```javascript
// get the path of current working file
var pa = app.getAbsoluteFilePath(app.getCurrentFileName(), ext = "")
var idx = pa.lastIndexOf("/")
var c_dir = pa.substr(0, idx) 
// run the script
cmd = system("python sortBib.py bibfilename.bib", workingDirectory=c_dir)
cmd.waitForFinished()
```
5. To run the Macro, click on the Macro name shown in the menu after clicking `Macros` on the top of TeXstudio

![Screen shot of macro setting]({{ site.baseurl}}/assets/pics/macro.png "Macro Setting")

Done!