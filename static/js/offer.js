// AJAX offer
const offerData = document.getElementById('bookin_offer')
$.ajax({
    type:'GET',
    url: '/dashboard/offer_json',
    success: function (response){
        console.log(response.data)
        const offer_data = response.data
        offer_data.map(item=>{
            const option = document.createElement('option')
            option.textContent = item.offer_name
            option.setAttribute('class','item')
            option.setAttribute('data-value',item.id)
            offerData.appendChild(option)
        })
    },
    error: function (error){
        console.log(error)
    }
})

offerData.addEventListener('change', e=>{
    console.log(e.target.value)
    const  selectedOffer = e.target.value

    $.ajax({
        type:'GET',
        url: `/dashboard/models_json/${selectedOffer}/`,
        success: function (response){
            console.log(response.data)
            const option = document.createElement('div')
            option.textContent = item.offer_name
            option.setAttribute('class','item')
            option.setAttribute('data-value',item.offer_name)
            offerData.appendChild(option)

        },
        error: function (error){
            console.log(error)
        }
    })

})
