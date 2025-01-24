import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Lütfen bir dosya seçin.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8080/upload-file', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setMessage(response.data.message);
    } catch (error) {
      setMessage('Dosya yükleme sırasında bir hata oluştu.');
    }
  };

  return (
    <div className="FileUpload">
      <h1>Dosya Yükleme</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Dosyayı Yükle</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default FileUpload;
