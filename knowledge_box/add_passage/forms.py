from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(FlaskForm):
    passage_name = StringField(
        label='Passage name',
        validators=[DataRequired()]
    )

    upload_type = SelectField(
        label='Select upload type',
        choices=[('Image', 'Image'), ('PDF', 'PDF')],
        validators=[DataRequired()]
    )

    file_upload = FileField(
        label='Upload file',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png', 'pdf'], 'Images and PDFs only!')
        ]
    )

    submit = SubmitField('Next')

    def validate_file_upload(form, field):
        if field.data:
            # Split the filename into a name and extension
            filename_parts = field.data.filename.rsplit('.', 1)
            if len(filename_parts) == 2:
                ext = filename_parts[1].lower()
                # Validate file extension based on upload type
                if form.upload_type.data == 'Image' and ext not in ['jpg', 'png']:
                    raise ValidationError('File does not match the selected upload type (Image).')
                elif form.upload_type.data == 'PDF' and ext != 'pdf':
                    raise ValidationError('File does not match the selected upload type (PDF).')
            else:
                raise ValidationError('Invalid file format.')


class TextForm(FlaskForm):
    passage_name = StringField(
        label='Passage name',
        validators=[DataRequired()]
    )

    passage_topic = SelectField(
        label='Passage topic',
        choices=[('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'),
                 ('Psychology', 'Psychology'), ('History', 'History')],
        validators=[DataRequired()]
    )

    passage_text = TextAreaField(
        label='Passage text',
        validators=[DataRequired()]
    )

    submit = SubmitField('Next')

