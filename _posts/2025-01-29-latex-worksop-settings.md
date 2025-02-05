---
layout: post
title: Setting forward search and inverse search in SumatraPDF for LaTeX-Workshop
---

To set up forward and inverse search in SumatraPDF using LaTeX Workshop extention in Visual Studio Code, follow these steps:
<!-- readmore -->

## Configure SumatraPDF
One of the following two methods can be used:
1. Method 1
   a. Open SumatraPDF.
   b. Go to `Settings` > `Options...`.
   c. In the `Inverse Search Command Line` field, enter the following command:
      
      ```plaintext
      "C:\path\to\Visual Studio Code\Code.exe" -r -g "%f:%l"
      ```

2. Input the following text into the `SumatraPDF-settings.txt` file located in the same directory as SumatraPDF:

```plaintext
InverseSearchCmdLine = "C:\\path\\to\\Visual Studio Code\\Code.exe" "%f" -line %l
``` 


## Configure LaTeX Workshop

1. Open your `settings.json` file in Visual Studio Code.
2. Add or update the following settings:

   ```json
   {
       "latex-workshop.latex.autoBuild.run": "onSave",       
       
       "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",

       "latex-workshop.view.pdf.viewer": "external",
       "latex-workshop.view.pdf.external.viewer.command": "D:\\Program Files\\SumatraPDF-3.5.2-64\\SumatraPDF-3.5.2-64.exe",
       "latex-workshop.view.pdf.external.viewer.args": [
           "-forward-search",
           "%TEX%",
           "%LINE%",
           "-reuse-instance",
           "-inverse-search",
           "\"C:\\Users\\liand\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" \"C:\\Users\\liand\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\out\\cli.js\" --ms-enable-electron-run-as-node -r -g \"%f:%l\"",
           "%PDF%"
       ],
       "latex-workshop.view.pdf.external.synctex.command": "D:\\Program Files\\SumatraPDF-3.5.2-64\\SumatraPDF-3.5.2-64.exe",
       "latex-workshop.view.pdf.external.synctex.args": [
           "-forward-search",
           "%TEX%",
           "%LINE%",
           "-reuse-instance",
           "-inverse-search",
           "\"C:\\Users\\liand\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" \"C:\\Users\\liand\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\out\\cli.js\" --ms-enable-electron-run-as-node -r -g \"%f:%l\"",
           "%PDF%"
       ]
   }
   ```