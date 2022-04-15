// import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function get_rand_challenge(data) {
    const url = `${BASE_URL}/generate-rand-challenge`;
    return axios.get(url, data)
}

export { get_rand_challenge }