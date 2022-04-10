// import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function upload(formData) {
    const url = `${BASE_URL}/imgs/upload`;
    return axios.post(url, formData)
        // get data
        .then(x => x.data)
        // add url field
        .then(x => x.data.map(img => Object.assign({},
            img, { url: `${BASE_URL}/uploads/${img.id}` })));
}

export { upload }