function sample() {
    const url = "/sample";
    const x = 3;

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            x: x
        })
    }

    // fetch(url, params).then()
    //     (response) => { console.log(response) };
    // ).catch(
    //     (error) => { console.log(error) }
    // );

    fetch(url, params)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.log(error));
}