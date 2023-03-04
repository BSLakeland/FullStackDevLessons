function sample() {
    const url = "/sample";
    const real = document.getElementById("realValue").value;
    const imag = document.getElementById("imagValue").value;

    console.log(real, imag);

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            real: real,
            imag: imag
        })
    }

    // fetch(url, params).then()
    //     (response) => { console.log(response) };
    // ).catch(
    //     (error) => { console.log(error) }
    // );

    fetch(url, params)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").value = data;
        })
        .catch(error => console.log(error));
}

function image() {
    const url = "/image";
    const real = document.getElementById("realValue").value;
    const imag = document.getElementById("imagValue").value;

    const width = document.getElementById("widthInput").value;
    const height = document.getElementById("heightInput").value;
    const zoom = document.getElementById("zoomInput").value;
    const maxIter = document.getElementById("maxIterInput").value;

    console.log(real, imag);

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            width: width,
            height: height,
            zoom: zoom,
            max_iter: maxIter
        })
    }

    // fetch(url, params).then()
    //     (response) => { console.log(response) };
    // ).catch(
    //     (error) => { console.log(error) }
    // );

    fetch(url, params)
        .then(response => response.blob())
        .then(blob => {
            const objextURL = URL.createObjectURL(blob);
            document.body.style.backgroundImage = `url(${objextURL})`;
            // document.getElementById("submit").disabled = false;
        })
        .catch(error => console.log(error));
}