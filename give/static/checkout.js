let elements;
let emailAddress = '';

// Handle Page Styles

document.querySelector("#submit").addEventListener("click", handleSubmit);
document.querySelector("#backbuttoncontainer").addEventListener("click", goBackToPriceSelect);
document.querySelector("#amount-selector-submit-button").addEventListener("click", runDonationProcess);

document.querySelector("#donate1").addEventListener("click", preset1);
document.querySelector("#donate2").addEventListener("click", preset2);
document.querySelector("#donate3").addEventListener("click", preset3);

async function preset1() {
    document.querySelector("#price-box").value = '10';
}
async function preset2() {
    document.querySelector("#price-box").value = '25';
}
async function preset3() {
    document.querySelector("#price-box").value = '50';
}

// returns the string 'invalid' if the user entered the price incorrectly, and
// a string representing the price if they entered it correctly; processes some
// common mistakes
function priceValidation(priceString) {
    
    price = priceString.trim();

    if (typeof price != 'string') {
        return 'invalid';
    } else {

        if (price.substring(0,1) == '$') {
            price = price.substring(1);
        }

        if (isNaN(price)) {
            return 'invalid';
        } else {
            return price;
        }
    }
}

function goBackToPriceSelect() {
    return
}

// runs validation, changes styles on page elements, then runs the
// initialize and checkstatus routines
async function runDonationProcess() {

    var d = String(document.querySelector("#price-box").value);

    if (priceValidation(d) == 'invalid') {
        let errorContainer = document.querySelector('#errorContainer');

        errorContainer.classList.remove('hidden')

    } else {    

        d = priceValidation(d);

        document.querySelector("#initial-container").classList.remove('h-[20rem]');
        document.querySelector("#initial-container").classList.add('h-0');
        document.querySelector("#donation-amount-container").innerHTML = d;

        setTimeout(function() {
            document.querySelector("#submit").classList.remove("hidden");
            document.querySelector("#price-label-container").classList.remove('hidden');
            document.querySelector("#price-label-container").classList.add('flex');

            initialize(d);
            checkStatus();
        }, 500);

    }
}


// Fetches a payment intent and captures the client secret
async function initialize(validatedPrice) {
    
    const response = await fetch("/create-payment-intent/"+String(validatedPrice) + "/", {
        method: "POST",
        headers: { 
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
    });


    const  { clientSecret } = await response.json();

    const appearance = {
        theme: 'stripe',
    };

    elements = stripe.elements({ appearance, clientSecret });


    const linkAuthenticationElement = elements.create("linkAuthentication");
    linkAuthenticationElement.mount("#link-authentication-element");

    linkAuthenticationElement.on('change', (event) => {
        emailAddress = event.value.email;
    });

    const paymentElementOptions = {
        layout: "tabs",
    };

    const paymentElement = elements.create("payment", paymentElementOptions);
    paymentElement.mount("#payment-element");


}

async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
        return_url: "http://localhost:8000/give/success",
        receipt_email: emailAddress,
        },
    });

    if (error.type === "card_error" || error.type === "validation_error") {
        showMessage(error.message);
    } else {
        showMessage("An unexpected error occurred.");
    }

    setLoading(false);

}

// Fetches the payment intent status after payment submission

async function checkStatus() {
    const clientSecret = new URLSearchParams(window.location.search).get(
        "payment_intent_client_secret"
    );

    if (!clientSecret) {
        return;
    }

    const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

    switch (paymentIntent.status) {
        case "succeeded":
        showMessage("Payment succeeded!");
        break;
        case "processing":
        showMessage("Your payment is processing.");
        break;
        case "requires_payment_method":
        showMessage("Your payment was not successful, please try again.");
        break;
        default:
        showMessage("Something went wrong.");
        break;
    }

}

// ------- UI helpers -------

function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageText.textContent = "";
    }, 4000);

}

// Show a spinner on payment submission
function setLoading(isLoading) {

    if (isLoading) {
        // Disable the button and show a spinner
        document.querySelector("#submit").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("#submit").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }

}