---
layout: post
title: Enhancing Your Markdown Editing Experience with Suggestions
---

To enable markdown suggestions in your markdown file, you can use the following tips:
<!-- readmore -->



1. **Use a Markdown Editor with Suggestions**: Choose a markdown editor that supports suggestions and autocompletion, such as Visual Studio Code with the Markdown All in One extension.

2. **Enable Extensions**: If you are using Visual Studio Code, install and enable extensions like "Markdown All in One" or "Markdown Preview Enhanced" to get suggestions and enhanced features.

3. **Configure Settings**: Ensure that the settings for your editor are configured to enable suggestions. For Visual Studio Code, you can add the following to your `settings.json` file:
    ```json
    {
        "[markdown]": {
            // 快速补全
            "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true
            },
            // 显示空格
            // "editor.renderWhitespace": "all",
            // snippet 提示优先（看个人喜欢）
            "editor.snippetSuggestions": "top",
            "editor.tabCompletion": "on",
            // 使用enter 接受提示
            // "editor.acceptSuggestionOnEnter": "on",
        },
    }
    ```

4. **Use Snippets**: Utilize markdown snippets to quickly insert common markdown structures. Most editors support snippets, and you can find or create snippets for your specific needs.

5. **Preview Your Markdown**: Use the preview feature in your markdown editor to see how your markdown will render in real-time. This can help you catch errors and improve your markdown formatting.

By following these steps, you can enhance your markdown editing experience with suggestions and other helpful features.