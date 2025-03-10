const loadInputs = async (value) => {
    const inputs = document.getElementById("inputs");

    if (!value) {
        inputs.innerHTML = "";
        return;
    }

    const response = await fetch(`./${value}_inputs.html`);
    const data = await response.text();

    inputs.innerHTML = data + "<button onclick='saveState()'>Send</button>";
    console.log("Insert form");
};

const loadState = async () => {
    if (!localStorage["cipherForm"]) {
        return;
    }

    console.log("Loading state...");

    const object = JSON.parse(localStorage["cipherForm"]);
    
    const cipherSelect = document.getElementById("cipher-select");
    cipherSelect.value = object["cipher-select"];

    document.querySelector("textarea[name='plain-text']").value = object["plain-text"];
    document.querySelector("input[name='to-upper']").checked = (object["to-upper"] == "on") ? true : false;

    await loadInputs(cipherSelect.value);
    
    console.log("Next action");

    const keys = Object.keys(object);
    const values = Object.values(object);

    let i0 = (object["to-upper"]) ? 3 : 2;

    for (let i = i0; i < keys.length; ++i) {
        console.log(keys[i]);
        document.querySelector(`input[name='${keys[i]}']`).value = values[i];
    }
        
};

const saveState = () => {
    console.log("Saving state...");
    

    const form = document.querySelector('#cipherForm');
    const cipherForm = new FormData(form);

    let object = {};

    cipherForm.forEach(function(value, key){
        object[key] = value;
    });

    localStorage.setItem( "cipherForm", JSON.stringify(object) );
};


document.querySelector('#cipher-select').addEventListener("change", async function() {
    console.log("Change event");
    await loadInputs(this.value);
});
  
