import io
import zipfile

from PIL import Image

from app import app


def make_png_bytes():
    buffer = io.BytesIO()
    Image.new('RGB', (64, 64), color=(30, 120, 40)).save(buffer, format='PNG')
    return buffer.getvalue()


def test_zip_upload_allows_three_hundred_images():
    client = app.test_client()
    with client.session_transaction() as session:
        session['email'] = 'demo@example.com'

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as archive:
        for index in range(300):
            archive.writestr(f'leaf_{index}.png', make_png_bytes())
    zip_buffer.seek(0)

    response = client.post(
        '/upload_dataset',
        data={'dataset': (io.BytesIO(zip_buffer.getvalue()), 'dataset.zip')},
        content_type='multipart/form-data',
    )

    assert response.status_code == 200, response.get_data(as_text=True)
    payload = response.get_json()
    assert payload['success'] is True
    assert payload['count'] >= 300
