var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);
        console.log('USER:', user);

        if (user === "AnonymousUser") {
            addCookie(productId, action)
        } else {
            updateUserOrder(productId, action)
        }
    });
}

function addCookie(productId, action){ 
     console.log('not logged in.......')
     if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }
        else{
            cart[productId]['quantity'] += 1
        }
     }
     if(action == 'remove'){
        cart[productId]['quantity'] -= 1
        if(cart[productId]['quantity'] <= 0){
            console.log('remove ')
            delete cart[productId]

        }

     }
     console.log("cart : " , cart)
     document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
     location.reload()
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
