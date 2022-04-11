// import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function perform_extract_colors(data) {
    const url = `${BASE_URL}/color-palette-extractor/perform/`;
    return axios.post(url, data)
        // get data
        // .then(x => x.colors)
        // add url field
        // .then(x => x.data.map(img => Object.assign({},
            // img, { url: `${BASE_URL}/uploads/${img.id}` })));
}

export { perform_extract_colors }