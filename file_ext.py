def declare_extensions(name, extensions):
    files_name = name.split()
    keys = extensions.split()

    # If more than one file is declared
    if len(files_name) > 1:
        test = files_name.map(name)
        print(test)
        for name in files_name:
            values = {
                "py": f"{name}.py",
                "less": f"{name}.less",
                "js": f"{name}.js",
                "ts": f"{name}.ts",
                "tsx": f"{name}.tsx",
                "sass": f"{name}.sass",
                "sb_tsx": f"{name}.stories.tsx",
                "sb_ts": f"{name}.stories.ts",
                "sb_js": f"{name}.stories.js",
                "test_js": f"{name}.test.js",
                "test_ts": f"{name}.test.ts",
                "test_tsx": f"{name}.test.tsx",
                "html": f"{name}.html",
                "css": f"{name}.css",
                "c++": f"{name}.cpp",
                "txt": f"{name}.txt",
                "pkg": f"{name}.pkg",
                "csv": f"{name}.csv",
                "sql": f"{name}.sql",
                "xml": f"{name}.xml",
                "bin": f"{name}.bin",
                "fon": f"{name}.fnt",
                "jsp": f"{name}.jsp",
                "php": f"{name}.php",
                "ppt": f"{name}.ppt",
                "c": f"{name}.c",
                "java_class": f"{name}.class",
                "bash_sh": f"{name}.sh",
                "swift": f"{name}.swift",
                "xls": f"{name}.xls",
                "md": f"{name}.md",
            }
            files = list(map(values.get, keys))
            for file in files:
                with open(file, "a+") as f:
                    f.write("export {};")
                    f.close()
    else:
        values = {
            "py": f"{name}.py",
            "less": f"{name}.less",
            "js": f"{name}.js",
            "ts": f"{name}.ts",
            "tsx": f"{name}.tsx",
            "sass": f"{name}.sass",
            "sb_tsx": f"{name}.stories.tsx",
            "sb_ts": f"{name}.stories.ts",
            "sb_js": f"{name}.stories.js",
            "test_js": f"{name}.test.js",
            "test_ts": f"{name}.test.ts",
            "test_tsx": f"{name}.test.tsx",
            "html": f"{name}.html",
            "css": f"{name}.css",
            "c++": f"{name}.cpp",
            "txt": f"{name}.txt",
            "pkg": f"{name}.pkg",
            "csv": f"{name}.csv",
            "sql": f"{name}.sql",
            "xml": f"{name}.xml",
            "bin": f"{name}.bin",
            "fon": f"{name}.fnt",
            "jsp": f"{name}.jsp",
            "php": f"{name}.php",
            "ppt": f"{name}.ppt",
            "c": f"{name}.c",
            "java_class": f"{name}.class",
            "bash_sh": f"{name}.sh",
            "swift": f"{name}.swift",
            "xls": f"{name}.xls",
            "md": f"{name}.md",
        }
        files = list(map(values.get, keys))

        # If one filename is declared
        for file in files:
            with open(file, "a+") as f:
                f.write("export {};")
                f.close()
