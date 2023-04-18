from django.forms.widgets import Textarea
from django.utils.html import format_html_join

class TinyMCEWidget(Textarea):
    def __init__(self, attrs=None):
        self.attrs = {'class': 'tinymce', 'rows': 10, 'cols': 80}
        if attrs is not None:
            self.attrs.update(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)

        script = """<script type="text/javascript">
                        tinymce.init({
                            selector: '#id_%s',
                            height: 500,
                            plugins: [
                                'advlist autolink lists link image charmap print preview anchor',
                                'searchreplace visualblocks code fullscreen',
                                'insertdatetime media table paste code help wordcount'
                            ],
                            toolbar: 'undo redo | formatselect | bold italic underline | \
                                      alignleft aligncenter alignright alignjustify | \
                                      bullist numlist outdent indent | removeformat | help',
                            content_css: '//www.tiny.cloud/css/codepen.min.css',
                        });
                    </script>
                 """

        return format_html_join(
            '\n', rendered + script, ((name,),)
        )
