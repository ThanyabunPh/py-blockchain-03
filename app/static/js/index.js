function posting_data() {
    const sender_data = document.getElementById('sender_address').value
    const sender_address = sender_data.split('_');
    const reciever_address = document.getElementById('reciever_address').value
    const amount = document.getElementById('amount').value

    if (sender_address[0] !== '' && reciever_address !== '' && amount !== '') {
        Swal.fire({
            title: 'Confirm your Transaction.',
            width: 600,
            showCancelButton: true,
            confirmButtonText: 'Accept',
            icon: 'warning',
            text: 'Sending to: ' + reciever_address + '\n' +
                'Amount: ' + amount
        }).then((result) => {

            if (result.isConfirmed) {
                Swal.fire({
                    title: 'Loading',
                    html: 'Auto close when completed',
                    allowOutsideClick: false,
                    didOpen: () => {
                        Swal.showLoading();
                        fetch('/send', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                "sender_address": sender_address[0],
                                "sender_private_key": sender_address[1],
                                "receiver_address": reciever_address,
                                "amount": amount
                            })
                        }).then(response => {
                            if (!response.ok) {
                                throw new Error(response.statusText)
                            } else {
                                Swal.fire({
                                    icon: 'success',
                                    title: 'Your request has completed',
                                    willClose:  () => {
                                        location.reload(); // refresh the page
                                    }
                                })
                            }
                        })
                    }
                })

            }
        })
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Please recheck Any input field.'
        })
    }
}

function check_balance() {
    address = document.getElementById('Balance_address').value
    if (address === '') {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Please recheck Any input field.'
        })
    } else {
        Swal.fire({
            title: 'Loading',
            html: 'Auto close when completed',
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
                fetch('/balance', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "address": address
                    })
                }).then((response) => response.json())
                    .then((data) => {
                        Swal.fire({
                            icon: 'success',
                            title: 'Your request has completed',
                            html: 'ETH: ' + data['ether'] + '<br>' +
                                  'gwei: ' + data['wei'] / 1000000000000000000 + ' x 10<sub style="vertical-align:super;">18</sub>'
                        })
                    })
            }
        })
    }
}