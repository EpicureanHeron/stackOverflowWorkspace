let arr = [2, 3, 4];
function m(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 1; j < 10; j++) {
            if (arr[i] % j === 0) {
                product = arr[i] * j
                console.log(j, arr[i], product )

            }
        }
    }
}

m(arr)