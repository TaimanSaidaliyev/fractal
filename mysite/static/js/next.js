
const getResourse = async () => {
    let url = 'http://localhost:8000/todo/json';
    const response = await fetch(url);
    if(!response.ok) {
        throw new Error(`Ошибка по адресу ${url}, статус ошибки ${response.status}`)
    };
    return response.json();
};

export function table_generation()
{
    const data = JSON.stringify(getResourse());
    for(key in data){
        let row = document.createElement('tr');
        row.innerHTML = `<td>${key}</td>`
        document.querySelector('.tat').appendChild(row)
    }
    console.log('Да сюда заходит');
};

console.log(getResourse())


