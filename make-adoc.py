import os
import re

def create_adoc_files():
    # 파일 이름 목록
    file_names = [
        "using-jquery-core.adoc",
        "dollar.adoc",
        "document-ready.adoc",
        "avoiding-conflicts-with-other-libraries.adoc",
        "attributes.adoc",
        "selecting-elements.adoc",
        "working-with-selections.adoc",
        "manipulating-elements.adoc",
        "the-jquery-object.adoc",
        "traversing.adoc",
        "css-styling-dimensions.adoc",
        "data-methods.adoc",
        "utility-methods.adoc",
        "iterating-over-jquery-and-non-jquery-objects.adoc",
        "using-jquerys-index-function.adoc",
        "frequently-asked-questions.adoc",
        "how-do-i-select-an-item-using-class-or-id.adoc",
        "how-do-i-select-elements-when-i-already-have-a-dom-element.adoc",
        "how-do-i-test-whether-an-element-has-a-particular-class.adoc",
        "how-do-i-test-whether-an-element-exists.adoc",
        "how-do-i-determine-the-state-of-a-toggled-element.adoc",
        "how-do-i-select-an-element-by-an-id-that-has-characters-used-in-css-notation.adoc",
        "how-do-i-disable-enable-a-form-element.adoc",
        "how-do-i-check-uncheck-a-checkbox-input-or-radio-button.adoc",
        "how-do-i-get-the-text-value-of-a-selected-option.adoc",
        "how-do-i-replace-text-from-the-3rd-element-of-a-list-of-10-items.adoc",
        "how-do-i-pull-a-native-dom-element-from-a-jquery-object.adoc"
    ]

    # 현재 디렉토리 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for file_name in file_names:
        # 파일 경로 생성
        file_path = os.path.join(current_dir, file_name)
        
        # 파일이 이미 존재하지 않으면 생성
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                # 파일 이름에서 제목 추출
                title = re.sub(r'[-_]', ' ', os.path.splitext(file_name)[0]).title()
                f.write(f"= {title}\n\n")
                f.write("내용을 여기에 작성하세요.\n")
            print(f"파일 생성됨: {file_name}")
        else:
            print(f"파일이 이미 존재함: {file_name}")

if __name__ == "__main__":
    create_adoc_files()