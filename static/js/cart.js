var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);
        console.log('USER:', user);

        if (user === "AnonymousUser") {
            console.log('user is not logged in');
        } else {
            updateUserOrder(productId, action)
        }
    });
}



function updateUserOrder(productId, action) {
    console.log('user is logged in , sending data')
    var url = 'update_Item';

    fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getToken('csrftoken')
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
