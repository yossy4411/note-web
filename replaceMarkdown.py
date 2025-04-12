def resolve_path(original_path):
    # ..みたいな相対パスを消す
    result = []
    for a in original_path.split("/"):
        if a == ".":
            continue
        elif a == "..":
            result.pop()
        else:
            result.append(a)

    return "/".join(result)

import re
from pathlib import Path

directory = Path("content")

# スラッグをキャッシュする

slug_cache = {}
for file in directory.rglob("*.md"):
    with open(file, "r", encoding="utf-8") as file_reader:
        lines = file_reader.readlines()
        property_detected = False
        toml = False
        for line in lines:
            line = str(line) # strに変換
            if not property_detected:
                if line.startswith("---"):
                    property_detected = True
                    continue
                if line.startswith("+++"):
                    property_detected = True
                    toml = True
                    continue
            else:
                # frontmatterの中のslugを取得する
                if line.startswith("slug"):
                    if toml:
                        slug = line.split("=")[1].strip().strip('"')
                    else:
                        slug = line.split(":")[1].strip()
                    break
                if line.startswith("---") or line.startswith("+++"):
                    slug = str(file.name.removesuffix(".md"))
                    break
        path = str(file.relative_to(directory)).removeprefix("./")
        slug_cache[path] = slug

for file in directory.rglob("*.md"):
    # ファイルの読み込み
    with open(file, "r", encoding="utf-8") as file_reader:
        document = '\n'.join(file_reader.readlines())

        path = str(file.relative_to(directory).parent)
        # 先ず、リンクを絶対パスに置き換える。
        def replace_links(match):
            link_text:str = match.group(1)
            original_url:str = match.group(2)
            if "://" in original_url:  # 外部リンク(https://, http://, ftp://など) を除外する
                return match.group(0)
            elif original_url.startswith("#"):  # セクションリンクを除外する
                return match.group(0)
            else: # 内部リンク
                # ここで、相対パスを絶対パスに変換する処理を行う
                # 例えば、URLが "/blog/example.md" から飛ぶ "../docs/guide.md" のリンクの場合、"/docs/guide.md" に変換する
                if path == "/":
                    file_url = f"{original_url}"
                else:
                    file_url = f"{path}/{original_url}"
                # さらに、相対パス表記を消す
                file_url_absolute = resolve_path(file_url)
                if file_url_absolute.endswith(".md"):
                    # Markdownファイルへのリンク
                    if not file_url_absolute in slug_cache:
                        # 存在しないファイルに対するリンクである。
                        # Hugoのショートコードに変換する。(dead link)
                        return f"{{< dead {file_url_absolute} >}}"
                    prefix = '/'.join(file_url_absolute.split("/")[:-1])
                    if prefix == "":
                        destination = slug_cache[file_url_absolute]
                    else:
                        destination = prefix + '/' + slug_cache[file_url_absolute]
                    if not destination.startswith("/"):
                        destination = '/' + destination
                    if not destination.endswith("/"):
                        destination += "/"
                    destination = destination.lower()
                else:
                    # 通常のファイルまたはディレクトリへのリンク
                    destination = '/' + file_url_absolute
                print(f'{original_url}\n -> {destination}')
                return f'[{link_text}]({file_url})'

        replaced1 = re.sub(r'\[(.*?)\]\((.*?)\)', replace_links, document)

        # 次に、アドモニションをショートコードの形に置き換える。
        # replaced2 = replaceMarkdown.replace_admonition_to_shortcode(replaced1)

