import {table_generation} from './next.js';

let bool;
let like_count = document.querySelector('.js_var_count').value;
let var_is_liked = document.querySelector('.js_var_bool').value;
let var_user = document.querySelector('.js_var_user').value;
let var_news_id = document.querySelector('.js_var_news_id').value;
let url = `news/like/${var_news_id}/${var_user}`;

if (var_is_liked == 'Yes'){
    bool = 1;
}
else {
    bool = 0;
};

is_liked(bool);

document.querySelector('[name="like_count"]').innerHTML = like_count;
document.querySelector('[name="check"]').innerHTML = url;

function get_request_username(){
    var username = 'Taiman';
    return username;
}

const press_like_button = async (user) =>
{
    var username = get_request_username();
    let url = 'http://localhost:8000/main/news/like/50/6';
    if (user == username){
        if (bool == 0)
        {
            let response = await fetch(url);
            bool = 1;
            like_count = like_count + 1;
            is_liked(bool);
        }
        else {
            let response = await fetch(url);
            bool = 0;
            like_count = like_count - 1;
            is_liked(bool);
        };
    };
    document.querySelector('[name="like_button"]').className = is_liked(bool);
    document.querySelector('[name="like_count"]').innerHTML = `${like_count}`;
    console.log(is_liked(bool));
}

function is_liked(is_liked){
    var class_name = '';
    var user = 'Taiman';
    if (user == get_request_username())
    {
        if (is_liked == 1)
        {
            class_name = 'nav-link btn btn-sm btn-color-danger btn-active-color-danger fw-bold px-4 me-1'
        }
        else
        {
            class_name = 'nav-link btn btn-sm btn-color-primary btn-active-color-primary fw-bold px-4 me-1'
        };
    };

    return class_name;
};

document.querySelector('[name="like_button"]').onclick = function (){
    press_like_button('Taiman');
};
