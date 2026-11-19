# Payments Integration (Stripe) Interview Questions and Answers

_Last updated: November 19, 2026_

450 interview questions with answers about integrating payments with Stripe, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target the current Stripe API (the Endive release line, `2026-09-30.endive` and the monthly versions after it) and the official Node.js SDK, `stripe` v23. Code examples use Node.js with ES modules. Some questions are about payments in general (cards, disputes, PCI, ledgers), because interviewers ask about those too, and they apply to any provider. Older APIs like the Charges API, the Card Element and subscription-level billing periods are mentioned where you'll still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Stripe?](#1-what-is-stripe)
- [2: What is the difference between a payment gateway and a payment processor?](#2-what-is-the-difference-between-a-payment-gateway-and-a-payment-processor)
- [3: Who are the parties in a card payment?](#3-who-are-the-parties-in-a-card-payment)
- [4: What is the difference between authorization and capture?](#4-what-is-the-difference-between-authorization-and-capture)
- [5: What is settlement and what is a payout?](#5-what-is-settlement-and-what-is-a-payout)
- [6: What is a chargeback?](#6-what-is-a-chargeback)
- [7: What is PCI DSS?](#7-what-is-pci-dss)
- [8: How does Stripe reduce your PCI scope?](#8-how-does-stripe-reduce-your-pci-scope)
- [9: What is the difference between a publishable key and a secret key?](#9-what-is-the-difference-between-a-publishable-key-and-a-secret-key)
- [10: What are restricted API keys?](#10-what-are-restricted-api-keys)
- [11: What are test mode and sandboxes?](#11-what-are-test-mode-and-sandboxes)
- [12: How do you set up the Stripe Node.js SDK?](#12-how-do-you-set-up-the-stripe-nodejs-sdk)
- [13: Why does Stripe use amounts in the smallest currency unit?](#13-why-does-stripe-use-amounts-in-the-smallest-currency-unit)
- [14: What are zero-decimal currencies?](#14-what-are-zero-decimal-currencies)
- [15: What is a PaymentIntent?](#15-what-is-a-paymentintent)
- [16: What are the possible statuses of a PaymentIntent?](#16-what-are-the-possible-statuses-of-a-paymentintent)
- [17: What is the client secret of a PaymentIntent?](#17-what-is-the-client-secret-of-a-paymentintent)
- [18: What is a PaymentMethod?](#18-what-is-a-paymentmethod)
- [19: What is a Customer object?](#19-what-is-a-customer-object)
- [20: What is a Charge and how does it relate to a PaymentIntent?](#20-what-is-a-charge-and-how-does-it-relate-to-a-paymentintent)
- [21: What is Stripe Checkout?](#21-what-is-stripe-checkout)
- [22: How do you create a Checkout Session?](#22-how-do-you-create-a-checkout-session)
- [23: Can you treat the success_url redirect as proof of payment?](#23-can-you-treat-the-success_url-redirect-as-proof-of-payment)
- [24: What are Payment Links?](#24-what-are-payment-links)
- [25: What is Stripe Elements?](#25-what-is-stripe-elements)
- [26: What is the Payment Element?](#26-what-is-the-payment-element)
- [27: How do you load Stripe.js?](#27-how-do-you-load-stripejs)
- [28: How do you confirm a payment on the client with the Payment Element?](#28-how-do-you-confirm-a-payment-on-the-client-with-the-payment-element)
- [29: What is the return_url used for?](#29-what-is-the-return_url-used-for)
- [30: When would you choose Checkout, Elements or Payment Links?](#30-when-would-you-choose-checkout-elements-or-payment-links)
- [31: What is a webhook?](#31-what-is-a-webhook)
- [32: Why are webhooks needed for payments?](#32-why-are-webhooks-needed-for-payments)
- [33: Which webhook events are most common in a payment integration?](#33-which-webhook-events-are-most-common-in-a-payment-integration)
- [34: How do you test webhooks on your local machine?](#34-how-do-you-test-webhooks-on-your-local-machine)
- [35: Which test card numbers do you use most?](#35-which-test-card-numbers-do-you-use-most)
- [36: What is 3D Secure?](#36-what-is-3d-secure)
- [37: What is SCA?](#37-what-is-sca)
- [38: What is idempotency and how does Stripe support it?](#38-what-is-idempotency-and-how-does-stripe-support-it)
- [39: What is metadata in Stripe?](#39-what-is-metadata-in-stripe)
- [40: What are the limits on metadata?](#40-what-are-the-limits-on-metadata)
- [41: How do you refund a payment?](#41-how-do-you-refund-a-payment)
- [42: How do you make a partial refund?](#42-how-do-you-make-a-partial-refund)
- [43: What are Products and Prices?](#43-what-are-products-and-prices)
- [44: What is the difference between a one-time price and a recurring price?](#44-what-is-the-difference-between-a-one-time-price-and-a-recurring-price)
- [45: What is a Subscription in Stripe?](#45-what-is-a-subscription-in-stripe)
- [46: What is an Invoice in Stripe?](#46-what-is-an-invoice-in-stripe)
- [47: What is the Customer Portal?](#47-what-is-the-customer-portal)
- [48: What is the Stripe Dashboard used for by developers?](#48-what-is-the-stripe-dashboard-used-for-by-developers)
- [49: What is a SetupIntent?](#49-what-is-a-setupintent)
- [50: What does setup_future_usage do?](#50-what-does-setup_future_usage-do)
- [51: What is the difference between on-session and off-session payments?](#51-what-is-the-difference-between-on-session-and-off-session-payments)
- [52: What is a statement descriptor?](#52-what-is-a-statement-descriptor)
- [53: What is the difference between a refund and a dispute?](#53-what-is-the-difference-between-a-refund-and-a-dispute)
- [54: Who pays for a dispute?](#54-who-pays-for-a-dispute)
- [55: How do Stripe fees work, and should you hardcode them?](#55-how-do-stripe-fees-work-and-should-you-hardcode-them)
- [56: What is a balance transaction?](#56-what-is-a-balance-transaction)
- [57: What is the difference between the pending and the available balance?](#57-what-is-the-difference-between-the-pending-and-the-available-balance)
- [58: How does Stripe API versioning work?](#58-how-does-stripe-api-versioning-work)
- [59: What does the expand parameter do?](#59-what-does-the-expand-parameter-do)
- [60: How does pagination work in the Stripe API?](#60-how-does-pagination-work-in-the-stripe-api)
- [61: How does auto-pagination work in the Node SDK?](#61-how-does-auto-pagination-work-in-the-node-sdk)
- [62: What is the difference between retrieve, list and search?](#62-what-is-the-difference-between-retrieve-list-and-search)
- [63: What types of errors can the Stripe API return?](#63-what-types-of-errors-can-the-stripe-api-return)
- [64: What is a decline code?](#64-what-is-a-decline-code)
- [65: Does the Stripe API have rate limits?](#65-does-the-stripe-api-have-rate-limits)
- [66: What is Stripe Radar?](#66-what-is-stripe-radar)
- [67: What is Link?](#67-what-is-link)
- [68: How do you accept Apple Pay and Google Pay?](#68-how-do-you-accept-apple-pay-and-google-pay)
- [69: Why do you need to register a domain for Apple Pay?](#69-why-do-you-need-to-register-a-domain-for-apple-pay)
- [70: What are local payment methods?](#70-what-are-local-payment-methods)
- [71: What are dynamic payment methods?](#71-what-are-dynamic-payment-methods)
- [72: What does the processing status mean for some payment methods?](#72-what-does-the-processing-status-mean-for-some-payment-methods)
- [73: How do bank debits like ACH and SEPA differ from cards?](#73-how-do-bank-debits-like-ach-and-sepa-differ-from-cards)
- [74: What is the difference between presentment currency and settlement currency?](#74-what-is-the-difference-between-presentment-currency-and-settlement-currency)
- [75: How do you sell in several currencies?](#75-how-do-you-sell-in-several-currencies)
- [76: What is Adaptive Pricing?](#76-what-is-adaptive-pricing)
- [77: What is Stripe Tax?](#77-what-is-stripe-tax)
- [78: What are coupons and promotion codes?](#78-what-are-coupons-and-promotion-codes)
- [79: How do you let customers enter promotion codes in Checkout?](#79-how-do-you-let-customers-enter-promotion-codes-in-checkout)
- [80: How do free trials work with subscriptions?](#80-how-do-free-trials-work-with-subscriptions)
- [81: What are the possible statuses of a subscription?](#81-what-are-the-possible-statuses-of-a-subscription)
- [82: What are the possible statuses of an invoice?](#82-what-are-the-possible-statuses-of-an-invoice)
- [83: How do you cancel a subscription?](#83-how-do-you-cancel-a-subscription)
- [84: How do you change a customer's plan?](#84-how-do-you-change-a-customers-plan)
- [85: What is proration?](#85-what-is-proration)
- [86: How do customers get receipts?](#86-how-do-customers-get-receipts)
- [87: What is Stripe Connect?](#87-what-is-stripe-connect)
- [88: What are typical use cases for Stripe Connect?](#88-what-are-typical-use-cases-for-stripe-connect)
- [89: What is an application fee?](#89-what-is-an-application-fee)
- [90: How are connected accounts onboarded?](#90-how-are-connected-accounts-onboarded)
- [91: How do you find a specific API request in Stripe's logs?](#91-how-do-you-find-a-specific-api-request-in-stripes-logs)
- [92: What does a Stripe Event object contain?](#92-what-does-a-stripe-event-object-contain)
- [93: What is the webhook signing secret?](#93-what-is-the-webhook-signing-secret)
- [94: How should a webhook handler respond?](#94-how-should-a-webhook-handler-respond)
- [95: What are test clocks?](#95-what-are-test-clocks)
- [96: Which Stripe IDs should you store in your database?](#96-which-stripe-ids-should-you-store-in-your-database)
- [97: What is a PaymentIntent's lifecycle in a simple card payment?](#97-what-is-a-paymentintents-lifecycle-in-a-simple-card-payment)
- [98: Why should the PaymentIntent be created on the server?](#98-why-should-the-paymentintent-be-created-on-the-server)
- [99: What is fulfillment, and when should you do it?](#99-what-is-fulfillment-and-when-should-you-do-it)
- [100: What is the difference between checkout.session.completed and checkout.session.async_payment_succeeded?](#100-what-is-the-difference-between-checkoutsessioncompleted-and-checkoutsessionasync_payment_succeeded)
- [101: In what order should you create the order and the payment?](#101-in-what-order-should-you-create-the-order-and-the-payment)
- [102: What is a mandate?](#102-what-is-a-mandate)
- [103: What is the default payment method of a customer?](#103-what-is-the-default-payment-method-of-a-customer)
- [104: How do you save and remove payment methods for a customer?](#104-how-do-you-save-and-remove-payment-methods-for-a-customer)
- [105: How do you list a customer's saved cards?](#105-how-do-you-list-a-customers-saved-cards)
- [106: What happens to saved cards when they expire or get replaced?](#106-what-happens-to-saved-cards-when-they-expire-or-get-replaced)
- [107: What information do you get about a card?](#107-what-information-do-you-get-about-a-card)
- [108: What is a card fingerprint used for?](#108-what-is-a-card-fingerprint-used-for)
- [109: What are CVC and address checks?](#109-what-are-cvc-and-address-checks)
- [110: What is tokenization?](#110-what-is-tokenization)
- [111: Why shouldn't you store card numbers yourself?](#111-why-shouldnt-you-store-card-numbers-yourself)
- [112: What is the hosted invoice page?](#112-what-is-the-hosted-invoice-page)
- [113: What is the difference between charge_automatically and send_invoice?](#113-what-is-the-difference-between-charge_automatically-and-send_invoice)
- [114: What are price lookup keys?](#114-what-are-price-lookup-keys)
- [115: Can you change or delete a Price?](#115-can-you-change-or-delete-a-price)
- [116: What is tiered pricing?](#116-what-is-tiered-pricing)
- [117: How do you bill per seat?](#117-how-do-you-bill-per-seat)
- [118: What is usage-based billing?](#118-what-is-usage-based-billing)
- [119: How does Checkout handle the Customer object?](#119-how-does-checkout-handle-the-customer-object)
- [120: How do you charge an amount that isn't a saved Price in Checkout?](#120-how-do-you-charge-an-amount-that-isnt-a-saved-price-in-checkout)
- [121: What are the modes of a Checkout Session?](#121-what-are-the-modes-of-a-checkout-session)
- [122: How long is a Checkout Session valid?](#122-how-long-is-a-checkout-session-valid)
- [123: How do you show order details on the success page?](#123-how-do-you-show-order-details-on-the-success-page)
- [124: What is embedded Checkout?](#124-what-is-embedded-checkout)
- [125: How do you use Stripe in a React app?](#125-how-do-you-use-stripe-in-a-react-app)
- [126: How do mobile apps take payments with Stripe?](#126-how-do-mobile-apps-take-payments-with-stripe)
- [127: What is Stripe Terminal?](#127-what-is-stripe-terminal)
- [128: What is the difference between Stripe Payments and Stripe Billing?](#128-what-is-the-difference-between-stripe-payments-and-stripe-billing)
- [129: How do you collect a customer's tax ID?](#129-how-do-you-collect-a-customers-tax-id)
- [130: How long does a refund take to reach the customer?](#130-how-long-does-a-refund-take-to-reach-the-customer)
- [131: What statuses can a refund have?](#131-what-statuses-can-a-refund-have)
- [132: How do you cancel a PaymentIntent?](#132-how-do-you-cancel-a-paymentintent)
- [133: How should you store and use Stripe API keys in your app?](#133-how-should-you-store-and-use-stripe-api-keys-in-your-app)
- [134: What do you do if a secret key leaks?](#134-what-do-you-do-if-a-secret-key-leaks)
- [135: How do webhook signatures work at a high level?](#135-how-do-webhook-signatures-work-at-a-high-level)
- [136: How are Stripe event types named?](#136-how-are-stripe-event-types-named)
- [137: Do webhook events arrive in order?](#137-do-webhook-events-arrive-in-order)
- [138: Can the same webhook event arrive more than once?](#138-can-the-same-webhook-event-arrive-more-than-once)
- [139: What other Stripe CLI commands are useful?](#139-what-other-stripe-cli-commands-are-useful)
- [140: What is the livemode field?](#140-what-is-the-livemode-field)
- [141: How does the Stripe API accept parameters?](#141-how-does-the-stripe-api-accept-parameters)
- [142: What is an invoice item?](#142-what-is-an-invoice-item)
- [143: How do you change the payout schedule?](#143-how-do-you-change-the-payout-schedule)
- [144: What is a Quote in Stripe?](#144-what-is-a-quote-in-stripe)
- [145: Should you use the Stripe Customer ID as your user ID?](#145-should-you-use-the-stripe-customer-id-as-your-user-id)
- [146: What happens if you create a new Stripe customer on every checkout?](#146-what-happens-if-you-create-a-new-stripe-customer-on-every-checkout)
- [147: What is a payment method's billing details field?](#147-what-is-a-payment-methods-billing-details-field)
- [148: What is shipping address collection in Checkout?](#148-what-is-shipping-address-collection-in-checkout)
- [149: What is the minimum amount you can charge?](#149-what-is-the-minimum-amount-you-can-charge)
- [150: Where can you see why a payment failed?](#150-where-can-you-see-why-a-payment-failed)

### Moderate Questions (151-300)

- [151: How do you build a basic PaymentIntent endpoint on the server?](#151-how-do-you-build-a-basic-paymentintent-endpoint-on-the-server)
- [152: What is deferred intent creation?](#152-what-is-deferred-intent-creation)
- [153: What are confirmation tokens?](#153-what-are-confirmation-tokens)
- [154: How do you verify Stripe webhooks in Express?](#154-how-do-you-verify-stripe-webhooks-in-express)
- [155: Why does webhook signature verification need the raw body?](#155-why-does-webhook-signature-verification-need-the-raw-body)
- [156: How do you handle Stripe webhooks in a Next.js route handler?](#156-how-do-you-handle-stripe-webhooks-in-a-nextjs-route-handler)
- [157: How do you make a webhook handler idempotent?](#157-how-do-you-make-a-webhook-handler-idempotent)
- [158: Why process webhooks in a background queue?](#158-why-process-webhooks-in-a-background-queue)
- [159: How do you deal with webhook events arriving out of order?](#159-how-do-you-deal-with-webhook-events-arriving-out-of-order)
- [160: What is the difference between thin events and snapshot events?](#160-what-is-the-difference-between-thin-events-and-snapshot-events)
- [161: What are event destinations?](#161-what-are-event-destinations)
- [162: How does Stripe retry failed webhook deliveries?](#162-how-does-stripe-retry-failed-webhook-deliveries)
- [163: Why does the API version of a webhook endpoint matter?](#163-why-does-the-api-version-of-a-webhook-endpoint-matter)
- [164: How do you choose idempotency keys?](#164-how-do-you-choose-idempotency-keys)
- [165: What happens if you reuse an idempotency key with different parameters?](#165-what-happens-if-you-reuse-an-idempotency-key-with-different-parameters)
- [166: Does the Node SDK retry requests by itself?](#166-does-the-node-sdk-retry-requests-by-itself)
- [167: How do you handle Stripe errors in code?](#167-how-do-you-handle-stripe-errors-in-code)
- [168: How do you handle 3D Secure when you confirm on the server?](#168-how-do-you-handle-3d-secure-when-you-confirm-on-the-server)
- [169: How do you charge a saved card when the customer isn't present?](#169-how-do-you-charge-a-saved-card-when-the-customer-isnt-present)
- [170: How do you save a card with a SetupIntent?](#170-how-do-you-save-a-card-with-a-setupintent)
- [171: How do you authorize now and capture later?](#171-how-do-you-authorize-now-and-capture-later)
- [172: How long does an authorization last, and can it be extended?](#172-how-long-does-an-authorization-last-and-can-it-be-extended)
- [173: How do you connect refunds to your own data?](#173-how-do-you-connect-refunds-to-your-own-data)
- [174: How do you create a subscription with a custom payment form?](#174-how-do-you-create-a-subscription-with-a-custom-payment-form)
- [175: What changed about invoices and PaymentIntents in the Basil release?](#175-what-changed-about-invoices-and-paymentintents-in-the-basil-release)
- [176: Where do you find the current billing period of a subscription now?](#176-where-do-you-find-the-current-billing-period-of-a-subscription-now)
- [177: Which events should you use to give and remove subscription access?](#177-which-events-should-you-use-to-give-and-remove-subscription-access)
- [178: What happens when a subscription renewal payment fails?](#178-what-happens-when-a-subscription-renewal-payment-fails)
- [179: What are Smart Retries and dunning?](#179-what-are-smart-retries-and-dunning)
- [180: How do you upgrade a plan and charge the difference right away?](#180-how-do-you-upgrade-a-plan-and-charge-the-difference-right-away)
- [181: How do you show the customer what a plan change will cost before they confirm?](#181-how-do-you-show-the-customer-what-a-plan-change-will-cost-before-they-confirm)
- [182: How do you downgrade at the end of the billing period?](#182-how-do-you-downgrade-at-the-end-of-the-billing-period)
- [183: What are subscription schedules used for?](#183-what-are-subscription-schedules-used-for)
- [184: How do you cancel immediately and refund the unused time?](#184-how-do-you-cancel-immediately-and-refund-the-unused-time)
- [185: How do you pause a subscription?](#185-how-do-you-pause-a-subscription)
- [186: How do you offer a free trial without asking for a card?](#186-how-do-you-offer-a-free-trial-without-asking-for-a-card)
- [187: How do you set up metered billing with meters?](#187-how-do-you-set-up-metered-billing-with-meters)
- [188: What is the Entitlements API?](#188-what-is-the-entitlements-api)
- [189: How do you send a customer to the Customer Portal?](#189-how-do-you-send-a-customer-to-the-customer-portal)
- [190: How do you keep subscription data in your database in sync with Stripe?](#190-how-do-you-keep-subscription-data-in-your-database-in-sync-with-stripe)
- [191: How do you create a subscription with Checkout?](#191-how-do-you-create-a-subscription-with-checkout)
- [192: Where should metadata go when you use Checkout?](#192-where-should-metadata-go-when-you-use-checkout)
- [193: What is client_reference_id in Checkout?](#193-what-is-client_reference_id-in-checkout)
- [194: How do you write a safe fulfillment function for Checkout?](#194-how-do-you-write-a-safe-fulfillment-function-for-checkout)
- [195: How can you recover abandoned Checkout sessions?](#195-how-can-you-recover-abandoned-checkout-sessions)
- [196: How do you style the Payment Element?](#196-how-do-you-style-the-payment-element)
- [197: What is the Express Checkout Element?](#197-what-is-the-express-checkout-element)
- [198: How do you register payment method domains with the API?](#198-how-do-you-register-payment-method-domains-with-the-api)
- [199: When should you create the Stripe Customer for a user?](#199-when-should-you-create-the-stripe-customer-for-a-user)
- [200: Why shouldn't you look up customers by email with the Search API during checkout?](#200-why-shouldnt-you-look-up-customers-by-email-with-the-search-api-during-checkout)
- [201: How do you expand fields on list results?](#201-how-do-you-expand-fields-on-list-results)
- [202: How do you upgrade to a new Stripe API version safely?](#202-how-do-you-upgrade-to-a-new-stripe-api-version-safely)
- [203: How does the Node SDK decide which API version to use?](#203-how-does-the-node-sdk-decide-which-api-version-to-use)
- [204: How do you unit test code that calls Stripe?](#204-how-do-you-unit-test-code-that-calls-stripe)
- [205: How do you run integration tests against Stripe?](#205-how-do-you-run-integration-tests-against-stripe)
- [206: How do you test your webhook handler without Stripe sending events?](#206-how-do-you-test-your-webhook-handler-without-stripe-sending-events)
- [207: How do you test a subscription renewal with test clocks?](#207-how-do-you-test-a-subscription-renewal-with-test-clocks)
- [208: What are the charge types in Stripe Connect?](#208-what-are-the-charge-types-in-stripe-connect)
- [209: How do you create a destination charge?](#209-how-do-you-create-a-destination-charge)
- [210: How do you create a direct charge?](#210-how-do-you-create-a-direct-charge)
- [211: How do you use separate charges and transfers?](#211-how-do-you-use-separate-charges-and-transfers)
- [212: What does on_behalf_of do?](#212-what-does-on_behalf_of-do)
- [213: How do you know when a connected account can accept payments and get payouts?](#213-how-do-you-know-when-a-connected-account-can-accept-payments-and-get-payouts)
- [214: How do Connect webhooks differ from normal webhooks?](#214-how-do-connect-webhooks-differ-from-normal-webhooks)
- [215: How do refunds work with destination charges?](#215-how-do-refunds-work-with-destination-charges)
- [216: What are Connect embedded components?](#216-what-are-connect-embedded-components)
- [217: What are the connected account types, and what is Accounts v2?](#217-what-are-the-connected-account-types-and-what-is-accounts-v2)
- [218: How do you respond to a dispute through the API?](#218-how-do-you-respond-to-a-dispute-through-the-api)
- [219: Which dispute events should you handle?](#219-which-dispute-events-should-you-handle)
- [220: What are some useful Radar rules?](#220-what-are-some-useful-radar-rules)
- [221: How can you help Radar detect fraud better?](#221-how-can-you-help-radar-detect-fraud-better)
- [222: How do you handle rate limit errors from Stripe?](#222-how-do-you-handle-rate-limit-errors-from-stripe)
- [223: What is a lock_timeout error?](#223-what-is-a-lock_timeout-error)
- [224: How should you model payment status in your own database?](#224-how-should-you-model-payment-status-in-your-own-database)
- [225: How do you match payouts to the payments in them?](#225-how-do-you-match-payouts-to-the-payments-in-them)
- [226: How do you get the Stripe fee for a payment?](#226-how-do-you-get-the-stripe-fee-for-a-payment)
- [227: How do currency conversions show up in Stripe data?](#227-how-do-currency-conversions-show-up-in-stripe-data)
- [228: What should you avoid logging in a Stripe integration?](#228-what-should-you-avoid-logging-in-a-stripe-integration)
- [229: How would you use restricted keys in a system with several services?](#229-how-would-you-use-restricted-keys-in-a-system-with-several-services)
- [230: How do you secure a webhook endpoint?](#230-how-do-you-secure-a-webhook-endpoint)
- [231: How do you rotate a webhook signing secret without missing events?](#231-how-do-you-rotate-a-webhook-signing-secret-without-missing-events)
- [232: How do you create and send a one-off invoice?](#232-how-do-you-create-and-send-a-one-off-invoice)
- [233: What is a credit note?](#233-what-is-a-credit-note)
- [234: What is the customer credit balance?](#234-what-is-the-customer-credit-balance)
- [235: How do you verify a US bank account for ACH payments?](#235-how-do-you-verify-a-us-bank-account-for-ach-payments)
- [236: What should you know about SEPA Direct Debit?](#236-what-should-you-know-about-sepa-direct-debit)
- [237: How do you set a dynamic statement descriptor?](#237-how-do-you-set-a-dynamic-statement-descriptor)
- [238: How do you show Checkout and Elements in the customer's language?](#238-how-do-you-show-checkout-and-elements-in-the-customers-language)
- [239: What does the back end return for a mobile payment sheet?](#239-what-does-the-back-end-return-for-a-mobile-payment-sheet)
- [240: How do you stop a customer from paying twice by double-clicking?](#240-how-do-you-stop-a-customer-from-paying-twice-by-double-clicking)
- [241: Should you create a new PaymentIntent every time the checkout page loads?](#241-should-you-create-a-new-paymentintent-every-time-the-checkout-page-loads)
- [242: How do you update the amount when the cart changes?](#242-how-do-you-update-the-amount-when-the-cart-changes)
- [243: What should you do with PaymentIntents that are never paid?](#243-what-should-you-do-with-paymentintents-that-are-never-paid)
- [244: How do you handle a $0 checkout?](#244-how-do-you-handle-a-0-checkout)
- [245: Who should calculate totals with tax and discounts: you or Stripe?](#245-who-should-calculate-totals-with-tax-and-discounts-you-or-stripe)
- [246: How do you calculate the platform's application fee?](#246-how-do-you-calculate-the-platforms-application-fee)
- [247: What is latest_charge on a PaymentIntent?](#247-what-is-latest_charge-on-a-paymentintent)
- [248: How do you update your orders when a refund happens?](#248-how-do-you-update-your-orders-when-a-refund-happens)
- [249: What should your app do when a dispute is opened?](#249-what-should-your-app-do-when-a-dispute-is-opened)
- [250: What are early fraud warnings?](#250-what-are-early-fraud-warnings)
- [251: What would you monitor in a Stripe integration?](#251-what-would-you-monitor-in-a-stripe-integration)
- [252: How do you debug a failing API call?](#252-how-do-you-debug-a-failing-api-call)
- [253: How should you separate environments in a Stripe integration?](#253-how-should-you-separate-environments-in-a-stripe-integration)
- [254: How do you set up the same products and prices in every environment?](#254-how-do-you-set-up-the-same-products-and-prices-in-every-environment)
- [255: How do you type webhook events in TypeScript?](#255-how-do-you-type-webhook-events-in-typescript)
- [256: What should your handler do with event types it doesn't know?](#256-what-should-your-handler-do-with-event-types-it-doesnt-know)
- [257: When does Stripe finalize subscription invoices?](#257-when-does-stripe-finalize-subscription-invoices)
- [258: How do you add a one-time charge to a subscription's next invoice?](#258-how-do-you-add-a-one-time-charge-to-a-subscriptions-next-invoice)
- [259: What is the billing cycle anchor?](#259-what-is-the-billing-cycle-anchor)
- [260: How do you handle frequent seat changes without confusing the customer?](#260-how-do-you-handle-frequent-seat-changes-without-confusing-the-customer)
- [261: Can a subscription have several prices?](#261-can-a-subscription-have-several-prices)
- [262: How do you raise prices for existing subscribers?](#262-how-do-you-raise-prices-for-existing-subscribers)
- [263: How do you bill a company that pays by bank transfer every month?](#263-how-do-you-bill-a-company-that-pays-by-bank-transfer-every-month)
- [264: A customer's subscription is past_due. How do you let them fix it?](#264-a-customers-subscription-is-past_due-how-do-you-let-them-fix-it)
- [265: What is invoice.payment_action_required?](#265-what-is-invoicepayment_action_required)
- [266: How can Stripe help recover failed payments without code?](#266-how-can-stripe-help-recover-failed-payments-without-code)
- [267: How do you model a free plan?](#267-how-do-you-model-a-free-plan)
- [268: How do you let a customer switch from monthly to yearly?](#268-how-do-you-let-a-customer-switch-from-monthly-to-yearly)
- [269: How do you collect a reason when a customer cancels?](#269-how-do-you-collect-a-reason-when-a-customer-cancels)
- [270: How do you add custom fields to Checkout?](#270-how-do-you-add-custom-fields-to-checkout)
- [271: How do you let customers change quantity in Checkout?](#271-how-do-you-let-customers-change-quantity-in-checkout)
- [272: How do you connect Payment Link purchases to your users?](#272-how-do-you-connect-payment-link-purchases-to-your-users)
- [273: How do you redirect customers after paying with a Payment Link?](#273-how-do-you-redirect-customers-after-paying-with-a-payment-link)
- [274: How would you migrate from the Charges API and Card Element to current APIs?](#274-how-would-you-migrate-from-the-charges-api-and-card-element-to-current-apis)
- [275: Should your order point to a Checkout Session or a PaymentIntent?](#275-should-your-order-point-to-a-checkout-session-or-a-paymentintent)
- [276: How do you send a customer straight to a specific action in the Customer Portal?](#276-how-do-you-send-a-customer-straight-to-a-specific-action-in-the-customer-portal)
- [277: How do you calculate tax with a custom Elements checkout?](#277-how-do-you-calculate-tax-with-a-custom-elements-checkout)
- [278: How do you collect addresses in an Elements checkout?](#278-how-do-you-collect-addresses-in-an-elements-checkout)
- [279: When would one app use several Stripe accounts?](#279-when-would-one-app-use-several-stripe-accounts)
- [280: What should you watch out for when handling webhooks in serverless functions?](#280-what-should-you-watch-out-for-when-handling-webhooks-in-serverless-functions)
- [281: How do you structure a handler that supports many event types?](#281-how-do-you-structure-a-handler-that-supports-many-event-types)
- [282: How do you map Stripe objects to your own data model?](#282-how-do-you-map-stripe-objects-to-your-own-data-model)
- [283: How do discounts work on subscriptions in current API versions?](#283-how-do-discounts-work-on-subscriptions-in-current-api-versions)
- [284: How do you limit who can use a promotion code?](#284-how-do-you-limit-who-can-use-a-promotion-code)
- [285: How do you clean up subscriptions that never got paid?](#285-how-do-you-clean-up-subscriptions-that-never-got-paid)
- [286: Should your app call Stripe on every request to check if a user has paid?](#286-should-your-app-call-stripe-on-every-request-to-check-if-a-user-has-paid)
- [287: What is a grace period, and how do you implement it?](#287-what-is-a-grace-period-and-how-do-you-implement-it)
- [288: How do you implement a refund on cancellation policy?](#288-how-do-you-implement-a-refund-on-cancellation-policy)
- [289: How do you let a customer retry a failed one-time payment?](#289-how-do-you-let-a-customer-retry-a-failed-one-time-payment)
- [290: How do you save a card with Checkout and charge it later?](#290-how-do-you-save-a-card-with-checkout-and-charge-it-later)
- [291: What is the difference between payment_intent.payment_failed and charge.failed?](#291-what-is-the-difference-between-payment_intentpayment_failed-and-chargefailed)
- [292: What happens when a payout fails?](#292-what-happens-when-a-payout-fails)
- [293: What reporting options does Stripe give you?](#293-what-reporting-options-does-stripe-give-you)
- [294: How are disputes on bank debits different from card disputes?](#294-how-are-disputes-on-bank-debits-different-from-card-disputes)
- [295: How do you test that a webhook handler handles failures correctly?](#295-how-do-you-test-that-a-webhook-handler-handles-failures-correctly)
- [296: What do you check before going live?](#296-what-do-you-check-before-going-live)
- [297: How do you make your Stripe data easy to find in the Dashboard?](#297-how-do-you-make-your-stripe-data-easy-to-find-in-the-dashboard)
- [298: What is the difference between a SetupIntent and saving a card during payment?](#298-what-is-the-difference-between-a-setupintent-and-saving-a-card-during-payment)
- [299: How do you handle Connect payouts in different currencies?](#299-how-do-you-handle-connect-payouts-in-different-currencies)
- [300: What are payment method configurations?](#300-what-are-payment-method-configurations)

### Advanced Questions (301-450)

- [301: How would you design the payments part of an e-commerce back end with Stripe?](#301-how-would-you-design-the-payments-part-of-an-e-commerce-back-end-with-stripe)
- [302: What is the source of truth for payment state: Stripe or your database?](#302-what-is-the-source-of-truth-for-payment-state-stripe-or-your-database)
- [303: How do you make sure an order is fulfilled exactly once?](#303-how-do-you-make-sure-an-order-is-fulfilled-exactly-once)
- [304: How do you avoid calling Stripe and then failing to save the result?](#304-how-do-you-avoid-calling-stripe-and-then-failing-to-save-the-result)
- [305: A payment succeeded in Stripe, but your server crashed before saving the order. What happens?](#305-a-payment-succeeded-in-stripe-but-your-server-crashed-before-saving-the-order-what-happens)
- [306: How do you design idempotency keys for a multi-step payment operation?](#306-how-do-you-design-idempotency-keys-for-a-multi-step-payment-operation)
- [307: How is idempotency different in the v2 API?](#307-how-is-idempotency-different-in-the-v2-api)
- [308: How do you handle the race between the success redirect and the webhook?](#308-how-do-you-handle-the-race-between-the-success-redirect-and-the-webhook)
- [309: Two webhook events for the same order are processed at the same time. How do you avoid a mess?](#309-two-webhook-events-for-the-same-order-are-processed-at-the-same-time-how-do-you-avoid-a-mess)
- [310: How would you process webhooks at high volume?](#310-how-would-you-process-webhooks-at-high-volume)
- [311: Your webhook endpoint was down for a day. How do you recover?](#311-your-webhook-endpoint-was-down-for-a-day-how-do-you-recover)
- [312: What stops someone from replaying an old signed webhook?](#312-what-stops-someone-from-replaying-an-old-signed-webhook)
- [313: How does Stripe's webhook signature verification work in detail?](#313-how-does-stripes-webhook-signature-verification-work-in-detail)
- [314: What are the trade-offs of thin events?](#314-what-are-the-trade-offs-of-thin-events)
- [315: How do you move to a new major API version when webhooks are involved?](#315-how-do-you-move-to-a-new-major-api-version-when-webhooks-are-involved)
- [316: The Endive release removed payment_method_types from PaymentIntent and Checkout create calls. How do you migrate?](#316-the-endive-release-removed-payment_method_types-from-paymentintent-and-checkout-create-calls-how-do-you-migrate)
- [317: How do you migrate from legacy usage records to Billing Meters?](#317-how-do-you-migrate-from-legacy-usage-records-to-billing-meters)
- [318: What is the flexible billing mode for subscriptions?](#318-what-is-the-flexible-billing-mode-for-subscriptions)
- [319: How would you design subscription access control in your app?](#319-how-would-you-design-subscription-access-control-in-your-app)
- [320: What are some tricky proration cases?](#320-what-are-some-tricky-proration-cases)
- [321: A customer downgrades and wants their money back. How do you handle it?](#321-a-customer-downgrades-and-wants-their-money-back-how-do-you-handle-it)
- [322: How do you build a reliable usage reporting pipeline for meters?](#322-how-do-you-build-a-reliable-usage-reporting-pipeline-for-meters)
- [323: How do invoices with partial payments affect your code?](#323-how-do-invoices-with-partial-payments-affect-your-code)
- [324: You're building a marketplace where buyers order from several sellers in one cart. Which charge type would you use?](#324-youre-building-a-marketplace-where-buyers-order-from-several-sellers-in-one-cart-which-charge-type-would-you-use)
- [325: What does merchant of record mean, and why does it matter for platforms?](#325-what-does-merchant-of-record-mean-and-why-does-it-matter-for-platforms)
- [326: What happens when a connected account's balance goes negative?](#326-what-happens-when-a-connected-accounts-balance-goes-negative)
- [327: How do you recover dispute losses on destination charges?](#327-how-do-you-recover-dispute-losses-on-destination-charges)
- [328: How do you handle changing verification requirements for connected accounts?](#328-how-do-you-handle-changing-verification-requirements-for-connected-accounts)
- [329: What is a card testing attack, and how do you defend against it?](#329-what-is-a-card-testing-attack-and-how-do-you-defend-against-it)
- [330: When should you ask for 3D Secure when it isn't required?](#330-when-should-you-ask-for-3d-secure-when-it-isnt-required)
- [331: How do you prepare for "friendly fraud" disputes?](#331-how-do-you-prepare-for-friendly-fraud-disputes)
- [332: How can you improve your payment authorization rate?](#332-how-can-you-improve-your-payment-authorization-rate)
- [333: Which failed payments should you retry, and which not?](#333-which-failed-payments-should-you-retry-and-which-not)
- [334: What are SCA exemptions and merchant-initiated transactions?](#334-what-are-sca-exemptions-and-merchant-initiated-transactions)
- [335: How do Checkout and Elements differ for PCI compliance?](#335-how-do-checkout-and-elements-differ-for-pci-compliance)
- [336: How do you set up a Content Security Policy for Stripe.js?](#336-how-do-you-set-up-a-content-security-policy-for-stripejs)
- [337: What are common authorization bugs in payment endpoints?](#337-what-are-common-authorization-bugs-in-payment-endpoints)
- [338: Can you trust metadata in webhook events?](#338-can-you-trust-metadata-in-webhook-events)
- [339: How do you protect your webhook endpoint from abuse?](#339-how-do-you-protect-your-webhook-endpoint-from-abuse)
- [340: Why would you build a ledger next to Stripe, and how would it look?](#340-why-would-you-build-a-ledger-next-to-stripe-and-how-would-it-look)
- [341: How would you build a daily reconciliation job?](#341-how-would-you-build-a-daily-reconciliation-job)
- [342: How do you record refunds, disputes and fees in your books?](#342-how-do-you-record-refunds-disputes-and-fees-in-your-books)
- [343: How do you stay within Stripe rate limits at scale?](#343-how-do-you-stay-within-stripe-rate-limits-at-scale)
- [344: How do you cache Stripe data safely?](#344-how-do-you-cache-stripe-data-safely)
- [345: Many workers update the same Stripe customer at once and get lock_timeout errors. What do you do?](#345-many-workers-update-the-same-stripe-customer-at-once-and-get-lock_timeout-errors-what-do-you-do)
- [346: How would you run a backfill over all your customers without hitting rate limits?](#346-how-would-you-run-a-backfill-over-all-your-customers-without-hitting-rate-limits)
- [347: How do you migrate customers and saved cards from another payment provider to Stripe?](#347-how-do-you-migrate-customers-and-saved-cards-from-another-payment-provider-to-stripe)
- [348: When does it make sense to use more than one payment processor?](#348-when-does-it-make-sense-to-use-more-than-one-payment-processor)
- [349: How should your app behave if Stripe has an outage?](#349-how-should-your-app-behave-if-stripe-has-an-outage)
- [350: A call to create a payment timed out. Did the customer get charged?](#350-a-call-to-create-a-payment-timed-out-did-the-customer-get-charged)
- [351: The customer paid but closed the browser during the 3D Secure redirect. How does your app find out?](#351-the-customer-paid-but-closed-the-browser-during-the-3d-secure-redirect-how-does-your-app-find-out)
- [352: How would you organize tests for a payment integration?](#352-how-would-you-organize-tests-for-a-payment-integration)
- [353: How would you use test clocks in CI?](#353-how-would-you-use-test-clocks-in-ci)
- [354: How do you protect yourself from breaking changes in Stripe responses?](#354-how-do-you-protect-yourself-from-breaking-changes-in-stripe-responses)
- [355: How do you trace a payment through your system?](#355-how-do-you-trace-a-payment-through-your-system)
- [356: What alerts would you set up for a payment system?](#356-what-alerts-would-you-set-up-for-a-payment-system)
- [357: How do you handle a GDPR deletion request for a customer with Stripe data?](#357-how-do-you-handle-a-gdpr-deletion-request-for-a-customer-with-stripe-data)
- [358: A marketplace needs to refund a buyer after the seller was already paid out. What happens?](#358-a-marketplace-needs-to-refund-a-buyer-after-the-seller-was-already-paid-out-what-happens)
- [359: How can a platform hold funds before paying sellers?](#359-how-can-a-platform-hold-funds-before-paying-sellers)
- [360: How would you handle payments for a service where the final amount isn't known at booking time?](#360-how-would-you-handle-payments-for-a-service-where-the-final-amount-isnt-known-at-booking-time)
- [361: How do you use a customer's saved card on a connected account?](#361-how-do-you-use-a-customers-saved-card-on-a-connected-account)
- [362: Where should customers live in a Connect platform: on the platform or on connected accounts?](#362-where-should-customers-live-in-a-connect-platform-on-the-platform-or-on-connected-accounts)
- [363: How do you handle a platform where sellers are in many countries?](#363-how-do-you-handle-a-platform-where-sellers-are-in-many-countries)
- [364: What are instant payouts and what should you watch out for?](#364-what-are-instant-payouts-and-what-should-you-watch-out-for)
- [365: How does manual review in Radar work in your system?](#365-how-does-manual-review-in-radar-work-in-your-system)
- [366: How do you design fulfillment for payment methods that can take days to settle?](#366-how-do-you-design-fulfillment-for-payment-methods-that-can-take-days-to-settle)
- [367: An ACH payment succeeded, but weeks later the money was taken back. How do you design for this?](#367-an-ach-payment-succeeded-but-weeks-later-the-money-was-taken-back-how-do-you-design-for-this)
- [368: How would you design checkout for customers in many countries?](#368-how-would-you-design-checkout-for-customers-in-many-countries)
- [369: What tax edge cases should a back-end developer know about?](#369-what-tax-edge-cases-should-a-back-end-developer-know-about)
- [370: Why can't you edit a finalized invoice, and how do you fix mistakes?](#370-why-cant-you-edit-a-finalized-invoice-and-how-do-you-fix-mistakes)
- [371: How do you migrate existing subscriptions from another billing system to Stripe?](#371-how-do-you-migrate-existing-subscriptions-from-another-billing-system-to-stripe)
- [372: How would you move thousands of subscribers to a new price?](#372-how-would-you-move-thousands-of-subscribers-to-a-new-price)
- [373: How do you keep seat counts in sync without too many updates?](#373-how-do-you-keep-seat-counts-in-sync-without-too-many-updates)
- [374: How would you model a plan with a base fee, included usage and overage?](#374-how-would-you-model-a-plan-with-a-base-fee-included-usage-and-overage)
- [375: How would you implement prepaid credits?](#375-how-would-you-implement-prepaid-credits)
- [376: How do you handle refunds for usage-based billing?](#376-how-do-you-handle-refunds-for-usage-based-billing)
- [377: What is revenue recognition, and why does it matter for subscriptions?](#377-what-is-revenue-recognition-and-why-does-it-matter-for-subscriptions)
- [378: When should you fetch from Stripe and when read your own copy?](#378-when-should-you-fetch-from-stripe-and-when-read-your-own-copy)
- [379: How do you route webhooks for several developers and environments?](#379-how-do-you-route-webhooks-for-several-developers-and-environments)
- [380: How do you type expandable fields safely in TypeScript?](#380-how-do-you-type-expandable-fields-safely-in-typescript)
- [381: What should you watch for when a webhook handler calls other services?](#381-what-should-you-watch-for-when-a-webhook-handler-calls-other-services)
- [382: What do you do with an event that always fails to process?](#382-what-do-you-do-with-an-event-that-always-fails-to-process)
- [383: How would you make sure you never miss a webhook event?](#383-how-would-you-make-sure-you-never-miss-a-webhook-event)
- [384: A customer says they were charged twice. How do you investigate?](#384-a-customer-says-they-were-charged-twice-how-do-you-investigate)
- [385: Webhook signature verification works locally but fails in production. What would you check?](#385-webhook-signature-verification-works-locally-but-fails-in-production-what-would-you-check)
- [386: A user's subscription is active in Stripe, but they lost access in your app. What could be wrong?](#386-a-users-subscription-is-active-in-stripe-but-they-lost-access-in-your-app-what-could-be-wrong)
- [387: The payment decline rate suddenly doubled. How do you investigate?](#387-the-payment-decline-rate-suddenly-doubled-how-do-you-investigate)
- [388: You see a card testing attack happening right now. What do you do?](#388-you-see-a-card-testing-attack-happening-right-now-what-do-you-do)
- [389: A payout is lower than finance expected. How do you explain it?](#389-a-payout-is-lower-than-finance-expected-how-do-you-explain-it)
- [390: Your dispute rate is rising. What would you do?](#390-your-dispute-rate-is-rising-what-would-you-do)
- [391: Payments get stuck in requires_action and never complete. What could be wrong?](#391-payments-get-stuck-in-requires_action-and-never-complete-what-could-be-wrong)
- [392: After upgrading the API version, invoices are no longer linked to payments in your system. What happened?](#392-after-upgrading-the-api-version-invoices-are-no-longer-linked-to-payments-in-your-system-what-happened)
- [393: An order was fulfilled twice. What would you check?](#393-an-order-was-fulfilled-twice-what-would-you-check)
- [394: During a big sale you get many 429 errors from Stripe. What do you do?](#394-during-a-big-sale-you-get-many-429-errors-from-stripe-what-do-you-do)
- [395: A customer changed plans five times in one day and their invoice is confusing. How do you prevent this?](#395-a-customer-changed-plans-five-times-in-one-day-and-their-invoice-is-confusing-how-do-you-prevent-this)
- [396: A refund failed. What now?](#396-a-refund-failed-what-now)
- [397: A seller's connected account was disabled, and they have money in their balance. What can the platform do?](#397-a-sellers-connected-account-was-disabled-and-they-have-money-in-their-balance-what-can-the-platform-do)
- [398: The success page says "paid" but your webhook says the session is unpaid. Why?](#398-the-success-page-says-paid-but-your-webhook-says-the-session-is-unpaid-why)
- [399: Customers say they don't recognize your charges. What do you change?](#399-customers-say-they-dont-recognize-your-charges-what-do-you-change)
- [400: Your webhook queue keeps growing during peak hours. How do you fix it?](#400-your-webhook-queue-keeps-growing-during-peak-hours-how-do-you-fix-it)
- [401: How would you build a one-click upsell after checkout?](#401-how-would-you-build-a-one-click-upsell-after-checkout)
- [402: How would you design payments for a marketplace that splits one order among many sellers?](#402-how-would-you-design-payments-for-a-marketplace-that-splits-one-order-among-many-sellers)
- [403: How would you design billing for a SaaS with a trial, per-seat pricing and usage add-ons?](#403-how-would-you-design-billing-for-a-saas-with-a-trial-per-seat-pricing-and-usage-add-ons)
- [404: How would you support custom donation amounts, one-time and monthly?](#404-how-would-you-support-custom-donation-amounts-one-time-and-monthly)
- [405: How would you add tips for workers on a Connect platform?](#405-how-would-you-add-tips-for-workers-on-a-connect-platform)
- [406: How would you build pre-orders that are charged when the product ships?](#406-how-would-you-build-pre-orders-that-are-charged-when-the-product-ships)
- [407: How would you implement a refundable deposit, like for a rental?](#407-how-would-you-implement-a-refundable-deposit-like-for-a-rental)
- [408: How would you handle B2B customers who pay invoices on net-30 terms?](#408-how-would-you-handle-b2b-customers-who-pay-invoices-on-net-30-terms)
- [409: Can a mobile app use Stripe to sell digital content?](#409-can-a-mobile-app-use-stripe-to-sell-digital-content)
- [410: How would you automate refunds while keeping control?](#410-how-would-you-automate-refunds-while-keeping-control)
- [411: A company has legal entities in the US, the EU and the UK. How would you set up Stripe?](#411-a-company-has-legal-entities-in-the-us-the-eu-and-the-uk-how-would-you-set-up-stripe)
- [412: How would you build an internal admin tool for payments?](#412-how-would-you-build-an-internal-admin-tool-for-payments)
- [413: How do you load Stripe.js without slowing down your pages?](#413-how-do-you-load-stripejs-without-slowing-down-your-pages)
- [414: What can go wrong on the front end, and how do you make checkout robust?](#414-what-can-go-wrong-on-the-front-end-and-how-do-you-make-checkout-robust)
- [415: What is special about three-decimal currencies?](#415-what-is-special-about-three-decimal-currencies)
- [416: How do you handle time and dates in Stripe data?](#416-how-do-you-handle-time-and-dates-in-stripe-data)
- [417: Why might a snapshot event not contain the data you need?](#417-why-might-a-snapshot-event-not-contain-the-data-you-need)
- [418: How long can you get past events from the API?](#418-how-long-can-you-get-past-events-from-the-api)
- [419: How do you delete a customer in your app without breaking things in Stripe?](#419-how-do-you-delete-a-customer-in-your-app-without-breaking-things-in-stripe)
- [420: What payment records should a company keep, and for how long?](#420-what-payment-records-should-a-company-keep-and-for-how-long)
- [421: You inherit a messy Stripe integration. How would you improve it?](#421-you-inherit-a-messy-stripe-integration-how-would-you-improve-it)
- [422: What do you look for when reviewing payment code?](#422-what-do-you-look-for-when-reviewing-payment-code)
- [423: How would you compare Stripe with other payment providers?](#423-how-would-you-compare-stripe-with-other-payment-providers)
- [424: What is the difference between using Stripe directly and using a merchant of record service?](#424-what-is-the-difference-between-using-stripe-directly-and-using-a-merchant-of-record-service)
- [425: What is the Stripe v2 API, and how is it different from v1?](#425-what-is-the-stripe-v2-api-and-how-is-it-different-from-v1)
- [426: Which Stripe Dashboard settings can change how your code behaves?](#426-which-stripe-dashboard-settings-can-change-how-your-code-behaves)
- [427: How do you look up Stripe data quickly when you have millions of customers?](#427-how-do-you-look-up-stripe-data-quickly-when-you-have-millions-of-customers)
- [428: How do you deploy webhook workers without losing events?](#428-how-do-you-deploy-webhook-workers-without-losing-events)
- [429: How do you roll out a risky change to the payment flow?](#429-how-do-you-roll-out-a-risky-change-to-the-payment-flow)
- [430: You just launched payments. What do you watch in the first week?](#430-you-just-launched-payments-what-do-you-watch-in-the-first-week)
- [431: What are the most common mistakes in Stripe integrations?](#431-what-are-the-most-common-mistakes-in-stripe-integrations)
- [432: How would you design payment collection for invoices your own system creates?](#432-how-would-you-design-payment-collection-for-invoices-your-own-system-creates)
- [433: How do you handle refunds from both your admin tool and the Stripe Dashboard?](#433-how-do-you-handle-refunds-from-both-your-admin-tool-and-the-stripe-dashboard)
- [434: How would you handle partial shipments for an order paid upfront?](#434-how-would-you-handle-partial-shipments-for-an-order-paid-upfront)
- [435: How would you let customers pay with store credit and a card together?](#435-how-would-you-let-customers-pay-with-store-credit-and-a-card-together)
- [436: How do you sell add-ons in the middle of a subscription period?](#436-how-do-you-sell-add-ons-in-the-middle-of-a-subscription-period)
- [437: How would you show customers their current usage and upcoming bill?](#437-how-would-you-show-customers-their-current-usage-and-upcoming-bill)
- [438: How do you stop people from abusing free trials?](#438-how-do-you-stop-people-from-abusing-free-trials)
- [439: How do you protect saved cards if a user's account is taken over?](#439-how-do-you-protect-saved-cards-if-a-users-account-is-taken-over)
- [440: What security issues can come up with Customer Portal and Checkout URLs?](#440-what-security-issues-can-come-up-with-customer-portal-and-checkout-urls)
- [441: In a B2B SaaS, should the Stripe customer be the user or the organization?](#441-in-a-b2b-saas-should-the-stripe-customer-be-the-user-or-the-organization)
- [442: How do tax rate changes affect existing subscriptions?](#442-how-do-tax-rate-changes-affect-existing-subscriptions)
- [443: How do you test Connect flows?](#443-how-do-you-test-connect-flows)
- [444: What is Smart Disputes?](#444-what-is-smart-disputes)
- [445: When would you choose Elements over Checkout, even though it's more work?](#445-when-would-you-choose-elements-over-checkout-even-though-its-more-work)
- [446: Why should you be careful when one action creates events on both the platform and a connected account?](#446-why-should-you-be-careful-when-one-action-creates-events-on-both-the-platform-and-a-connected-account)
- [447: What changed about webhook verification tolerance in the latest Node SDK major version?](#447-what-changed-about-webhook-verification-tolerance-in-the-latest-node-sdk-major-version)
- [448: A customer opens Checkout, and you change the price before they pay. What happens?](#448-a-customer-opens-checkout-and-you-change-the-price-before-they-pay-what-happens)
- [449: What records should you keep to explain payment decisions to finance or auditors?](#449-what-records-should-you-keep-to-explain-payment-decisions-to-finance-or-auditors)
- [450: You're the first engineer at a startup that needs to start charging customers. How would you set up payments?](#450-youre-the-first-engineer-at-a-startup-that-needs-to-start-charging-customers-how-would-you-set-up-payments)

---

# Easy Questions (1-150)

## 1: What is Stripe?

Stripe is a payment company that gives developers APIs to accept and manage payments online. You can take card payments, bank debits, wallets like Apple Pay, run subscriptions, send invoices and pay out money to other businesses.

It takes care of the hard parts: talking to banks and card networks, storing card data safely, fraud checks and most of the compliance work. You talk to it through a REST API and client libraries.

## 2: What is the difference between a payment gateway and a payment processor?

A payment gateway is the part that takes payment details from the customer and sends them securely to be processed. A payment processor moves the transaction through the card networks and banks and reports the result.

In the past these were often separate companies. Stripe does both, and it is also the acquirer's partner that settles the money to your bank account, so you only integrate with one provider.

## 3: Who are the parties in a card payment?

- Cardholder: the customer paying.
- Merchant: the business selling something.
- Issuer: the customer's bank that gave them the card. It approves or declines the payment.
- Acquirer: the merchant's bank (or a provider like Stripe working with one) that receives the money.
- Card network: Visa, Mastercard, American Express and so on. It connects issuers and acquirers and sets the rules.

## 4: What is the difference between authorization and capture?

Authorization asks the issuer if the customer can pay. If yes, the money is held on the card but not taken yet. Capture tells the issuer to actually take the held money.

By default Stripe does both in one step. You can split them, for example to hold money when an order is placed and capture it only when the item ships. For most cards an uncaptured authorization expires after about 7 days.

## 5: What is settlement and what is a payout?

Settlement is when the money from captured payments actually moves from the card networks to the acquirer. In Stripe this shows as funds moving from your pending balance to your available balance.

A payout is when Stripe sends money from your available Stripe balance to your bank account. Payouts usually run automatically on a schedule (for example daily), but you can also trigger them manually.

## 6: What is a chargeback?

A chargeback happens when the cardholder asks their bank to reverse a payment, for example because they don't recognize it or never got the product. The bank takes the money back from the merchant.

In Stripe this is called a dispute. The money and a dispute fee are taken from your balance right away, and you can send evidence to try to win the money back.

## 7: What is PCI DSS?

PCI DSS (Payment Card Industry Data Security Standard) is a set of security rules for every business that stores, processes or sends card data. It covers things like network security, encryption, access control and logging.

How much work you need to do depends on how card data touches your systems. If raw card numbers reach your servers, you have a lot to prove. If they never do, the requirements are much smaller.

## 8: How does Stripe reduce your PCI scope?

With Stripe Checkout, Elements or the mobile SDKs, card details are typed into fields hosted by Stripe (in an iframe or on a Stripe page). They go straight from the customer's browser to Stripe, and your server only gets IDs like `pm_...`.

Because raw card numbers never touch your servers, most businesses can use the simplest self-assessment form (SAQ A). Stripe is a PCI Level 1 service provider and handles the heavy part.

## 9: What is the difference between a publishable key and a secret key?

The publishable key (`pk_live_...` or `pk_test_...`) is safe to put in front-end code. It can only do limited things, like collect payment details with Stripe.js.

The secret key (`sk_live_...` or `sk_test_...`) can do anything on your account: create charges, refund, read customer data. It must stay on the server, in environment variables or a secret manager, and never in a Git repo or the browser.

## 10: What are restricted API keys?

Restricted keys (`rk_live_...`) are secret keys with limited permissions. You choose for each resource whether the key has no access, read access or write access.

Use them for services that only need part of the API, for example a reporting job that only reads balance transactions. If such a key leaks, the damage is much smaller than with a full secret key.

## 11: What are test mode and sandboxes?

Stripe has separate environments for testing. Test data uses test keys (`sk_test_...`), no real money moves, and you use special test card numbers.

Sandboxes are isolated test environments inside your account. Each one has its own keys, data and settings, so different teams or branches don't mix their test data. You will still see the older term "test mode" in many docs and projects.

## 12: How do you set up the Stripe Node.js SDK?

Install the package and create a client with your secret key:

```bash
npm install stripe
```

```js
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
```

The SDK uses the API version it was released with, and its TypeScript types match that version. Most examples in this file assume a `stripe` client created like this.

## 13: Why does Stripe use amounts in the smallest currency unit?

Amounts are integers in the smallest unit of the currency. For USD that is cents, so `amount: 1999` means $19.99.

Integers avoid rounding errors you get with floating point numbers, like `0.1 + 0.2 = 0.30000000000000004`. Your code should also store money as integers (or a decimal type in the database), never as floats.

## 14: What are zero-decimal currencies?

Some currencies don't have a smaller unit, like the Japanese yen (JPY) or the Korean won (KRW). For them you pass the amount as is: `amount: 500` with `currency: 'jpy'` means ¥500, not ¥5.

A few currencies have three decimals, like KWD and BHD. If you support many currencies, don't hardcode "multiply by 100". Use a small helper or table based on the currency.

## 15: What is a PaymentIntent?

A PaymentIntent is the object that tracks one payment from start to finish. You create it with an amount and a currency, and it moves through statuses until it succeeds or is canceled.

It handles retries, 3D Secure checks and different payment methods. One PaymentIntent should match one order or one cart in your app.

```js
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "usd",
  metadata: { orderId: "order_123" },
});
```

## 16: What are the possible statuses of a PaymentIntent?

- `requires_payment_method`: no payment method yet, or the last one failed.
- `requires_confirmation`: has a payment method, waiting to be confirmed.
- `requires_action`: the customer must do something, usually 3D Secure.
- `processing`: the payment is being processed (common for bank debits).
- `requires_capture`: authorized, waiting for you to capture it.
- `succeeded`: done, money will arrive.
- `canceled`: canceled, no more attempts possible.

When a payment fails, the PaymentIntent goes back to `requires_payment_method`, so the customer can try again.

## 17: What is the client secret of a PaymentIntent?

The `client_secret` is a key for one PaymentIntent. You send it to the front end so Stripe.js can confirm the payment there.

It is not as powerful as a secret key, but it does give access to that payment. Don't log it, don't put it in URLs and only send it to the customer who owns the payment.

## 18: What is a PaymentMethod?

A PaymentMethod (`pm_...`) is an object that holds a customer's payment details, like a card, a bank account or a wallet. Stripe keeps the sensitive data, and you only get safe parts, like the card brand, last 4 digits and expiry date.

You can use a PaymentMethod once, or attach it to a Customer to use it again later.

## 19: What is a Customer object?

A Customer (`cus_...`) represents a buyer in Stripe. It holds their email, name, address, saved payment methods, subscriptions and invoices.

Usually you create one Stripe Customer per user in your app and store its ID in your user table. Customers are needed for subscriptions, saved cards and invoices. For a one-time guest payment you don't strictly need one.

## 20: What is a Charge and how does it relate to a PaymentIntent?

A Charge (`ch_...`) is one attempt to move money. In current integrations you don't create Charges yourself. The PaymentIntent creates them when it is confirmed, and `paymentIntent.latest_charge` points to the most recent one.

Creating Charges directly with the Charges API is the legacy way. It does not handle 3D Secure well, so new code should use PaymentIntents or Checkout.

## 21: What is Stripe Checkout?

Checkout is a payment page built by Stripe. You create a Checkout Session on your server, send the customer to it (or embed it on your site), and Stripe handles the form, payment methods, 3D Secure, taxes, discounts and receipts.

It is the fastest way to accept payments, and Stripe recommends Checkout Sessions for most integrations. You can customize colors, logo and fields, but not the full layout.

## 22: How do you create a Checkout Session?

```js
const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [{ price: "price_123", quantity: 1 }],
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
  cancel_url: "https://example.com/cart",
});

res.redirect(303, session.url);
```

Stripe replaces `{CHECKOUT_SESSION_ID}` with the real ID, so the success page knows which session finished.

## 23: Can you treat the success_url redirect as proof of payment?

No. The customer may close the browser before the redirect happens, or someone could open the success URL by hand. Also, some payment methods (like bank debits) are not finished at redirect time.

Use the `checkout.session.completed` webhook (and the async events for delayed methods) to fulfill orders. On the success page you can retrieve the session to show a nice message, but the webhook should do the real work.

## 24: What are Payment Links?

Payment Links are shareable URLs to a Stripe-hosted payment page. You can create them in the Dashboard without code, or with the API. You can send them by email, put them in a social media bio or behind a button.

They are good for simple cases: selling a few products, donations, or invoices sent by hand. For carts and dynamic prices, Checkout Sessions created from your server are a better fit.

## 25: What is Stripe Elements?

Elements is a set of UI components from Stripe.js for building your own payment form on your site. The fields run inside Stripe-hosted iframes, so card data never touches your page's JavaScript, but they look like part of your page.

Use Elements when you want full control over the layout of the checkout page. It needs more code than Checkout.

## 26: What is the Payment Element?

The Payment Element is one Element that shows all the payment methods enabled for your account: cards, wallets, bank debits, local methods. It picks which ones to show based on the customer's location, currency and amount.

It replaced the older approach of building forms with separate elements like the Card Element. New integrations should use it.

## 27: How do you load Stripe.js?

Stripe.js must be loaded from `js.stripe.com`, not bundled or self-hosted. That way you always get the latest security and fraud detection code. The `@stripe/stripe-js` npm package is a small loader that adds the script for you:

```js
import { loadStripe } from "@stripe/stripe-js";

const stripe = await loadStripe("pk_test_...");
```

## 28: How do you confirm a payment on the client with the Payment Element?

```js
const elements = stripe.elements({ clientSecret });
const paymentElement = elements.create("payment");
paymentElement.mount("#payment-element");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: { return_url: "https://example.com/order/complete" },
  });
  if (error) showMessage(error.message);
});
```

If it works, the customer is redirected to `return_url`. If there is an error (for example a declined card), `confirmPayment` returns it and you show it on the form.

## 29: What is the return_url used for?

Some payment methods send the customer away from your site: to their bank for 3D Secure, to a banking app, or to a wallet. `return_url` is where Stripe sends them back afterwards.

Stripe adds `payment_intent` and `payment_intent_client_secret` to the URL, so your page can check the result. Like the Checkout success URL, it's not proof of payment. Use webhooks for fulfillment.

## 30: When would you choose Checkout, Elements or Payment Links?

- Payment Links: no code, simple fixed products or quick sales.
- Checkout: you want a working, well-converting payment page fast, with little code and little maintenance.
- Elements: you need a fully custom checkout page inside your app.

Most teams should start with Checkout and move to Elements only if they have a clear design or flow need it can't meet.

## 31: What is a webhook?

A webhook is an HTTP request that Stripe sends to your server when something happens in your account. For example, when a payment succeeds, Stripe sends a `POST` with a JSON event to a URL you set up.

Webhooks let your app react to things that happen outside of the user's request, like a subscription renewal or a dispute.

## 32: Why are webhooks needed for payments?

Many things happen in the background, not while your code is waiting:

- A bank debit can take days to succeed or fail.
- A subscription renews every month.
- The customer can close the tab after paying.
- A dispute can come weeks later.

Without webhooks, your app would miss these or have to keep polling the API. Webhooks are the reliable way to keep your database in sync with Stripe.

## 33: Which webhook events are most common in a payment integration?

- `checkout.session.completed`: a Checkout Session finished.
- `payment_intent.succeeded` and `payment_intent.payment_failed`.
- `invoice.paid` and `invoice.payment_failed`: for subscriptions.
- `customer.subscription.created`, `.updated` and `.deleted`.
- `charge.refunded`: a refund was made.
- `charge.dispute.created`: a dispute was opened.

Only subscribe to the events you handle. It cuts noise and load.

## 34: How do you test webhooks on your local machine?

Use the Stripe CLI. It forwards events from Stripe to your local server:

```bash
stripe login
stripe listen --forward-to localhost:3000/webhooks/stripe
```

The command prints a webhook signing secret (`whsec_...`) for local use. In another terminal you can fire test events:

```bash
stripe trigger payment_intent.succeeded
```

## 35: Which test card numbers do you use most?

- `4242 4242 4242 4242`: a Visa card that always succeeds.
- `4000 0000 0000 0002`: always declined (generic decline).
- `4000 0000 0000 9995`: declined for insufficient funds.
- `4000 0027 6000 3184`: always asks for 3D Secure.

Use any future expiry date and any CVC. In server-side tests you can also use test PaymentMethod IDs like `pm_card_visa`. Real card numbers don't work in test mode.

## 36: What is 3D Secure?

3D Secure (3DS) is an extra check where the card issuer asks the customer to prove it's really them, for example with a code in their banking app. If the check passes, liability for fraud chargebacks usually moves from the merchant to the issuer.

Stripe runs 3DS when the issuer or the law requires it, or when your Radar rules ask for it. With Checkout and the Payment Element, it's handled for you.

## 37: What is SCA?

Strong Customer Authentication (SCA) is a rule from the European PSD2 law. Many online payments from European customers need two of three factors: something they know (password), something they have (phone) and something they are (fingerprint).

For cards, SCA is usually done through 3D Secure. Stripe's PaymentIntents and SetupIntents were built to support SCA, which is one reason the old Charges API is legacy.

## 38: What is idempotency and how does Stripe support it?

An idempotent request can be sent many times with the same result as sending it once. That is important for payments: if a request times out, you want to retry without charging the customer twice.

Stripe accepts an idempotency key on `POST` requests. If you send the same key again, Stripe returns the saved result of the first request instead of doing it again.

```js
await stripe.paymentIntents.create(
  { amount: 2000, currency: "usd" },
  { idempotencyKey: `order_123_create_pi` },
);
```

## 39: What is metadata in Stripe?

Metadata is a set of your own key-value pairs that you can attach to most Stripe objects. It is commonly used to link Stripe objects to your data, like `{ orderId: '123', userId: '42' }`.

You get it back in API responses and webhooks, so your webhook handler can find the right order. Don't put sensitive data in metadata, like card numbers or passwords.

## 40: What are the limits on metadata?

You can have up to 50 keys. Keys can be up to 40 characters and can't contain square brackets. Values can be up to 500 characters and are always stored as strings.

If you need more data, store it in your database and put only the ID in metadata.

## 41: How do you refund a payment?

Create a Refund for the PaymentIntent:

```js
const refund = await stripe.refunds.create({
  payment_intent: "pi_123",
});
```

Without an `amount`, it refunds the full amount that's left. Stripe sends the money back to the original payment method. You can also refund from the Dashboard.

## 42: How do you make a partial refund?

Pass an `amount` smaller than the payment:

```js
await stripe.refunds.create({
  payment_intent: "pi_123",
  amount: 500, // refund $5.00
  reason: "requested_by_customer",
});
```

You can make several partial refunds until the full amount is refunded. `reason` can be `duplicate`, `fraudulent` or `requested_by_customer`.

## 43: What are Products and Prices?

A Product is what you sell, like "Pro plan" or "T-shirt". A Price says how much it costs and how it's billed: the amount, the currency and, for subscriptions, the interval (month, year).

One Product can have many Prices, for example monthly and yearly, or USD and EUR. Checkout, Payment Links and subscriptions all use Price IDs (`price_...`).

## 44: What is the difference between a one-time price and a recurring price?

A one-time price is charged once, for example a book. A recurring price is charged on a schedule, for example $10 per month, and is used with subscriptions.

```js
await stripe.prices.create({
  product: "prod_123",
  unit_amount: 1000,
  currency: "usd",
  recurring: { interval: "month" },
});
```

## 45: What is a Subscription in Stripe?

A Subscription charges a customer on a repeating schedule for one or more Prices. Each period, Stripe creates an Invoice and tries to pay it with the customer's saved payment method.

Subscriptions handle trials, plan changes, prorations, failed payment retries and cancellation. Your app usually gives or removes access based on the subscription's status.

## 46: What is an Invoice in Stripe?

An Invoice is a bill for a customer. It has line items, taxes, discounts and a total. Subscriptions create invoices automatically every period, and you can also create one-off invoices.

An invoice can be paid automatically with a saved payment method, or sent to the customer by email with a link to a hosted payment page. Stripe can also generate a PDF.

## 47: What is the Customer Portal?

The Customer Portal is a Stripe-hosted page where customers can manage their own billing: update their card, see and download invoices, change plans or cancel.

You configure what customers are allowed to do in the Dashboard, then create a portal session on your server and redirect the customer to it. It saves you from building all these pages yourself.

## 48: What is the Stripe Dashboard used for by developers?

Besides showing payments and customers, developers use the Dashboard (and its Workbench tools) to:

- See API request logs and the exact request and response bodies.
- See webhook events and delivery attempts, and resend them.
- Manage API keys and webhook endpoints.
- Turn payment methods on or off.
- Look at test data in sandboxes.

It is often the first place to look when something fails.

## 49: What is a SetupIntent?

A SetupIntent collects and saves a customer's payment method for later, without charging now. It runs any needed authentication (like 3D Secure) at setup time, so later off-session payments are more likely to go through.

Typical uses: a free trial that charges later, saving a card on an account settings page, or a service billed after it's delivered.

## 50: What does setup_future_usage do?

When you set `setup_future_usage` on a PaymentIntent, Stripe saves the payment method to the customer after the payment, ready for later use.

```js
await stripe.paymentIntents.create({
  amount: 2000,
  currency: "usd",
  customer: "cus_123",
  setup_future_usage: "off_session",
});
```

Use `off_session` if you'll charge later without the customer present, and `on_session` if they'll be in your checkout when you use it again. It is the way to "pay now and remember my card".

## 51: What is the difference between on-session and off-session payments?

An on-session payment happens while the customer is in your app and can respond, for example to a 3D Secure prompt. An off-session payment happens when they are not there, like a monthly renewal or a charge after a service is delivered.

Off-session payments can't ask the customer for anything, so the payment method should be set up in advance (with a SetupIntent or `setup_future_usage`). If the bank still asks for authentication, the payment fails and you have to bring the customer back.

## 52: What is a statement descriptor?

It is the text that shows up on the customer's bank or card statement, like `ACME* PRO PLAN`. A clear descriptor helps customers recognize the payment and avoids "I don't know this charge" disputes.

You set the default in the Dashboard. For card payments you can add a dynamic part per payment with `statement_descriptor_suffix`, for example an order number.

## 53: What is the difference between a refund and a dispute?

A refund is started by you, the merchant. You decide to give the money back, and there is no extra fee from the card network.

A dispute is started by the cardholder through their bank. The money is taken from you right away, a dispute fee is charged, and you have to send evidence to try to win it back. Too many disputes can get your account reviewed, so a quick refund is often better than a dispute.

## 54: Who pays for a dispute?

The merchant does. When a dispute is opened, Stripe takes the disputed amount and a dispute fee from your balance. If you win, the amount is returned. Whether the fee is returned depends on your pricing and region.

On Connect platforms, it depends on the charge type. With destination charges the platform is liable. With direct charges, the connected account is.

## 55: How do Stripe fees work, and should you hardcode them?

Stripe usually charges a percentage plus a fixed fee per successful payment, with extra fees for things like currency conversion, international cards, disputes and some products (Billing, Tax, Radar extras).

Don't hardcode fee rates in your code. They differ by country, payment method and contract, and they change. Read the actual fee from the payment's balance transaction instead.

## 56: What is a balance transaction?

A balance transaction (`txn_...`) is a record of money moving in or out of your Stripe balance: a payment, a refund, a fee, a dispute, a payout and so on. It shows `amount`, `fee`, `net` (amount minus fees) and `available_on` (when the money becomes available).

Balance transactions are the base for accounting and reconciliation, because every change to your balance has one.

## 57: What is the difference between the pending and the available balance?

When a payment succeeds, the money first goes to your pending balance. After a few days (depending on your country and account), it moves to the available balance.

Only the available balance can be paid out to your bank. Refunds are taken from the available balance first, then the pending one.

## 58: How does Stripe API versioning work?

Every request runs against an API version, which is a date and a name like `2026-09-30.endive`. Your account has a default version, and you can set another version per request with the `Stripe-Version` header (the SDKs set it for you).

Twice a year Stripe starts a new major release (like Basil, Clover, Dahlia, Endive) that can have breaking changes. The monthly releases inside a major release don't break anything. Your code only changes behavior when you choose to upgrade.

## 59: What does the expand parameter do?

Many fields hold only an ID of a related object, like `customer: 'cus_123'`. With `expand`, Stripe returns the full object in the same response, so you don't need a second request.

```js
const pi = await stripe.paymentIntents.retrieve("pi_123", {
  expand: ["customer", "latest_charge.balance_transaction"],
});
console.log(pi.customer.email);
```

You can expand nested fields with dots, up to four levels deep.

## 60: How does pagination work in the Stripe API?

List endpoints return up to `limit` items (default 10, max 100) and a `has_more` flag. To get the next page, pass the ID of the last item as `starting_after`:

```js
const page1 = await stripe.customers.list({ limit: 100 });
const lastId = page1.data.at(-1).id;
const page2 = await stripe.customers.list({
  limit: 100,
  starting_after: lastId,
});
```

`ending_before` goes the other way. This is cursor based, so it stays correct when new items are added.

## 61: How does auto-pagination work in the Node SDK?

List calls can be used with `for await`, and the SDK fetches the next pages for you:

```js
for await (const customer of stripe.customers.list({ limit: 100 })) {
  console.log(customer.id);
}
```

There is also `autoPagingEach()` and `autoPagingToArray({ limit: 1000 })`. `autoPagingToArray` requires a limit, so you don't load millions of objects into memory by accident.

## 62: What is the difference between retrieve, list and search?

- Retrieve gets one object by ID. It's the fastest and always up to date.
- List returns objects in order, with simple filters like `customer` or `created`.
- Search (for example `stripe.customers.search()`) uses a query language for more complex filters, like searching by email or metadata.

Search results are not immediate. New or updated data can take up to about a minute to appear, so don't use search right after creating something.

```js
const result = await stripe.customers.search({
  query: "email:'ana@example.com'",
});
```

## 63: What types of errors can the Stripe API return?

The main kinds are:

- Card errors: the card was declined or something is wrong with it. Show the message to the customer.
- Invalid request errors: wrong or missing parameters. A bug in your code.
- Authentication errors: wrong or missing API key.
- Permission errors: the key isn't allowed to do this (for example a restricted key).
- Rate limit errors: too many requests.
- API errors: something went wrong on Stripe's side.
- Connection errors: the network failed and you don't know if the request worked.

In the Node SDK these are classes like `Stripe.errors.StripeCardError` and `Stripe.errors.StripeInvalidRequestError`, so you can check them with `instanceof`.

## 64: What is a decline code?

When a card is declined, the error has `code: 'card_declined'` and a `decline_code` with more detail from the issuer, like `insufficient_funds`, `lost_card`, `expired_card` or `do_not_honor`.

Use it to decide what to do: ask for another card, ask the customer to contact their bank, or just retry later. Don't show codes like `stolen_card` to the customer. Show a generic message instead, so you don't help fraudsters.

## 65: Does the Stripe API have rate limits?

Yes. By default, in live mode an account can make about 100 requests per second in total, and about 25 per second in a sandbox or test mode. Some endpoints have lower limits of their own.

When you go over, you get an HTTP 429 error. The SDK can retry with backoff, but it's better to avoid hitting the limit by using webhooks instead of polling and by spreading out bulk jobs.

## 66: What is Stripe Radar?

Radar is Stripe's fraud detection. It looks at each payment using data from the whole Stripe network and gives it a risk score and level. High-risk payments are blocked by default.

With Radar for Fraud Teams you can write your own rules, like "block if the card country differs from the IP country and the amount is over $500", and put payments in a manual review queue.

## 67: What is Link?

Link is Stripe's saved-payment feature for customers. A customer saves their payment details once with their email and phone, and then can pay with one click on any site that uses Link through Stripe.

It works with Checkout and the Payment Element. It usually improves conversion for returning customers and doesn't need extra code once it's turned on.

## 68: How do you accept Apple Pay and Google Pay?

With Checkout and the Payment Element, wallets show up automatically when they are turned on in the Dashboard and the customer's device supports them. The Express Checkout Element shows wallet buttons (and Link) at the top of a page.

For Apple Pay on the web, you also need to register your domain with Stripe. Wallet payments are still card payments in the end, so you handle them the same way in your back end.

## 69: Why do you need to register a domain for Apple Pay?

Apple only shows Apple Pay on domains that were verified for the merchant. You register each domain (and subdomain) where the payment form appears, in the Dashboard or with the Payment Method Domains API.

If you forget, Apple Pay just doesn't appear, with no error for the customer. This is a common surprise when moving to a new domain or a staging environment.

## 70: What are local payment methods?

Local payment methods are the ways people pay in specific countries, other than international cards. Examples: iDEAL in the Netherlands, Bancontact in Belgium, SEPA Direct Debit in Europe, ACH Direct Debit in the US, Pix in Brazil, Klarna and Affirm (buy now, pay later).

Offering the right local methods can raise conversion a lot in those countries. With the Payment Element or Checkout, you turn them on in the Dashboard and Stripe shows the ones that fit the customer.

## 71: What are dynamic payment methods?

With dynamic payment methods, you choose which payment methods are allowed in the Dashboard, not in code. Stripe then shows the ones that fit each payment, based on currency, amount, country and device.

In current API versions you don't list payment method types when you create a PaymentIntent, SetupIntent or Checkout Session. The old `payment_method_types` parameter was removed from these create calls in the Endive release.

## 72: What does the processing status mean for some payment methods?

Some methods, especially bank debits like ACH or SEPA, don't give a result right away. After the customer confirms, the PaymentIntent goes to `processing`, and it can take several business days to become `succeeded` or fail.

Your app must handle this. Don't ship goods while it's `processing`, show the customer "payment pending", and wait for the `payment_intent.succeeded` or `payment_intent.payment_failed` webhook.

## 73: How do bank debits like ACH and SEPA differ from cards?

- They are cheaper, often a fixed or capped fee.
- They are slower: success or failure comes days later.
- The customer must agree to a mandate that allows you to debit their account.
- They can be reversed after success, for example when the customer disputes it with their bank.

They work well for large B2B payments and subscriptions, where the lower fee matters and a few days of delay is fine.

## 74: What is the difference between presentment currency and settlement currency?

The presentment currency is the one the customer sees and pays in, for example EUR. The settlement currency is the one that lands in your Stripe balance and bank account, for example USD.

If they differ, Stripe converts the money and charges a conversion fee. You can avoid conversion by having bank accounts in the currencies you sell in.

## 75: How do you sell in several currencies?

You can create a separate Price for each currency, or one Price with `currency_options`, which holds the amount for other currencies:

```js
await stripe.prices.create({
  product: "prod_123",
  currency: "usd",
  unit_amount: 1000,
  currency_options: {
    eur: { unit_amount: 900 },
    gbp: { unit_amount: 800 },
  },
});
```

Checkout then shows the right currency for the customer's location. Adaptive Pricing is another option, where Stripe converts the price for you.

## 76: What is Adaptive Pricing?

Adaptive Pricing lets Checkout show prices in the customer's local currency, converted automatically from your price. The customer pays in their own currency, which usually improves conversion, and you get the amount in your currency.

It's available with Checkout Sessions. You turn it on in the Dashboard, and you don't need to set prices for each currency yourself.

## 77: What is Stripe Tax?

Stripe Tax calculates and collects sales tax, VAT and GST based on the customer's location and what you sell. It works with Checkout, Invoicing, Billing and Payment Links, and also has a tax calculation API for custom flows.

You add tax registrations for the places where you must collect tax, then turn on automatic tax:

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [{ price: "price_123", quantity: 1 }],
  automatic_tax: { enabled: true },
  success_url: "https://example.com/success",
});
```

It calculates and reports the tax, but filing returns is still your job (or a partner's).

## 78: What are coupons and promotion codes?

A coupon defines a discount: a percent or a fixed amount, and how long it lasts (once, for some months, forever). A promotion code is a customer-facing code, like `SUMMER20`, that points to a coupon and can have its own limits, like an expiry date or one use per customer.

You apply discounts to a subscription, invoice or Checkout Session using the `discounts` array.

## 79: How do you let customers enter promotion codes in Checkout?

Set `allow_promotion_codes: true`:

```js
await stripe.checkout.sessions.create({
  mode: "subscription",
  line_items: [{ price: "price_pro_monthly", quantity: 1 }],
  allow_promotion_codes: true,
  success_url: "https://example.com/success",
});
```

Checkout shows a field for the code and checks it. If you want to apply a specific discount yourself instead, pass `discounts: [{ promotion_code: 'promo_123' }]`. You can't use both in the same session.

## 80: How do free trials work with subscriptions?

You can start a subscription with a trial using `trial_period_days` or `trial_end`. During the trial the status is `trialing`, and no payment is taken. When the trial ends, Stripe creates the first invoice and charges the saved payment method.

```js
await stripe.subscriptions.create({
  customer: "cus_123",
  items: [{ price: "price_pro_monthly" }],
  trial_period_days: 14,
});
```

Stripe sends `customer.subscription.trial_will_end` three days before the trial ends, which is a good time to remind the customer.

## 81: What are the possible statuses of a subscription?

- `trialing`: in a free trial.
- `active`: paid and in good standing.
- `incomplete`: the first payment hasn't succeeded yet.
- `incomplete_expired`: the first payment wasn't completed in time (about 23 hours).
- `past_due`: a renewal payment failed, Stripe is retrying.
- `unpaid`: retries ran out and the subscription stays open but unpaid (depends on your settings).
- `canceled`: ended.
- `paused`: paused, for example after a trial ended with no payment method.

Your app should decide which statuses give access, usually `active` and `trialing`.

## 82: What are the possible statuses of an invoice?

- `draft`: being prepared, can still be changed.
- `open`: finalized and waiting for payment.
- `paid`: paid in full.
- `uncollectible`: you don't expect to get paid (for reporting bad debt).
- `void`: canceled, it should not be paid.

Once an invoice is finalized, you can't edit its lines. To correct it, void it or issue a credit note.

## 83: How do you cancel a subscription?

To cancel right away:

```js
await stripe.subscriptions.cancel("sub_123");
```

To cancel at the end of the current period, so the customer keeps access until then:

```js
await stripe.subscriptions.update("sub_123", { cancel_at_period_end: true });
```

The second option is what most SaaS products do. The customer can undo it before the period ends by setting it back to `false`.

## 84: How do you change a customer's plan?

Update the subscription item with the new price:

```js
const sub = await stripe.subscriptions.retrieve("sub_123");

await stripe.subscriptions.update("sub_123", {
  items: [{ id: sub.items.data[0].id, price: "price_business_monthly" }],
});
```

Pass the existing item's `id`. If you leave it out, Stripe adds a second item instead of replacing the first, and the customer pays for both plans.

## 85: What is proration?

Proration means charging or crediting the difference when a plan changes in the middle of a billing period. If a customer upgrades from $10 to $30 halfway through the month, they get a credit for the unused half of the $10 plan and are charged for half of the $30 plan.

Stripe calculates this for you. You control it with `proration_behavior`: `create_prorations` (the default), `always_invoice` (bill the difference right away) or `none`.

## 86: How do customers get receipts?

Stripe can email receipts automatically for successful payments and refunds. You turn this on in the Dashboard. For a single payment you can set `receipt_email` on the PaymentIntent.

Invoices have their own emails and a hosted page with a PDF. Receipts are not sent in test mode, but you can preview them from the Dashboard.

## 87: What is Stripe Connect?

Connect is Stripe's product for platforms and marketplaces that move money between several parties. Your platform has its own Stripe account, and each seller or service provider gets a connected account.

You can take payments from customers, keep a fee and send the rest to the connected accounts. Stripe handles onboarding, identity checks (KYC) and payouts for those accounts.

## 88: What are typical use cases for Stripe Connect?

- Marketplaces: Etsy-style shops, where buyers pay and sellers receive the money.
- On-demand services: ride sharing or delivery, where drivers get paid.
- SaaS platforms: software for gyms or salons that lets each business accept payments from its own customers.
- Crowdfunding and donations to many organizations.

If your app only sells your own products, you don't need Connect.

## 89: What is an application fee?

An application fee is the platform's cut of a payment made through Connect. You set it per payment with `application_fee_amount`, and Stripe moves that amount to the platform's balance, while the rest goes to the connected account.

```js
await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  application_fee_amount: 1000, // platform keeps $10
  transfer_data: { destination: "acct_123" },
});
```

## 90: How are connected accounts onboarded?

The simplest way is Stripe-hosted onboarding. You create the account, then an Account Link, and redirect the user to it:

```js
const link = await stripe.accountLinks.create({
  account: "acct_123",
  refresh_url: "https://example.com/connect/refresh",
  return_url: "https://example.com/connect/done",
  type: "account_onboarding",
});
res.redirect(link.url);
```

Stripe collects the business and identity details. You can also embed onboarding in your site with Connect embedded components.

## 91: How do you find a specific API request in Stripe's logs?

Every response has a request ID (`req_...`) in the `Request-Id` header. The Node SDK exposes it on responses and errors (for example `err.requestId`). Log it together with your own order or user ID.

With the request ID, you can find the exact request and response in the Dashboard logs, and Stripe support can look it up too.

## 92: What does a Stripe Event object contain?

An Event (`evt_...`) has:

- `id`: unique, use it to skip duplicates.
- `type`: for example `invoice.paid`.
- `created`: a Unix timestamp in seconds.
- `data.object`: the object the event is about, as it was when the event happened.
- `data.previous_attributes`: for `.updated` events, the fields that changed and their old values.
- `livemode` and `api_version`.
- `account`: for Connect events, the connected account it came from.

This is the "snapshot" format. Newer "thin" events only carry a reference to the object, which you fetch yourself.

## 93: What is the webhook signing secret?

Each webhook endpoint has a signing secret that starts with `whsec_`. Stripe uses it to sign every event it sends, and your server uses it to check that the event really came from Stripe and wasn't changed.

It is different from your API key. Store it as a secret, and use the right one for each environment. The Stripe CLI gives you a separate one when you run `stripe listen`.

## 94: How should a webhook handler respond?

Return a 2xx status code as soon as you have verified and safely stored (or queued) the event. Do slow work, like sending emails or calling other APIs, after that or in a background job.

If you return an error, time out or redirect, Stripe treats the delivery as failed and retries it. In live mode, it keeps retrying with backoff for up to three days.

## 95: What are test clocks?

Test clocks let you move time forward in a sandbox to test billing. You create a clock, attach customers to it, create subscriptions, then advance the clock by a month to see renewals, trial ends and failed payments happen right away.

```js
const clock = await stripe.testHelpers.testClocks.create({
  frozen_time: Math.floor(Date.now() / 1000),
});
const customer = await stripe.customers.create({ test_clock: clock.id });
```

Without them, you'd have to wait for real time to pass to test a renewal.

## 96: Which Stripe IDs should you store in your database?

Store the IDs that link your data to Stripe:

- `cus_...` on your user or account.
- `sub_...` and its status on your subscription record.
- `pi_...` or `cs_...` (Checkout Session) on your order.
- `price_...` on your plan table.
- `acct_...` for connected accounts on Connect.

Don't store card details. With these IDs you can find the right Stripe object fast and match webhooks to your data.

## 97: What is a PaymentIntent's lifecycle in a simple card payment?

1. Your server creates the PaymentIntent with an amount. Status: `requires_payment_method`.
2. The customer enters their card in the Payment Element.
3. The client confirms the payment. If the bank asks for 3DS, the status is `requires_action` until the customer finishes it.
4. The payment is authorized and captured. Status: `succeeded`.
5. Stripe sends `payment_intent.succeeded`, and your webhook fulfills the order.

If the card is declined, the status goes back to `requires_payment_method` and the customer can try another card.

## 98: Why should the PaymentIntent be created on the server?

The server knows the real price. If the browser decided the amount, a user could change it to $0.01 with the developer tools. Creating the PaymentIntent also needs your secret key, which must never be in the browser.

So the browser sends what it wants to buy (product IDs and quantities), and the server looks up the prices, calculates the total and creates the PaymentIntent.

## 99: What is fulfillment, and when should you do it?

Fulfillment is what you do after the customer pays: ship the item, give access to the course, send the license key, mark the order as paid.

Do it when you get a reliable signal that the payment succeeded, usually a webhook like `checkout.session.completed` (with `payment_status: 'paid'`) or `payment_intent.succeeded`. Make it safe to run more than once, because the same event can arrive twice.

## 100: What is the difference between checkout.session.completed and checkout.session.async_payment_succeeded?

`checkout.session.completed` fires when the customer finishes Checkout. For cards the payment is usually done at that point, and the session's `payment_status` is `paid`.

For delayed methods like bank debits, the session completes with `payment_status: 'unpaid'`. Days later Stripe sends `checkout.session.async_payment_succeeded` or `checkout.session.async_payment_failed`. Handle all three events and only fulfill when the payment is really paid.

## 101: In what order should you create the order and the payment?

A common order is:

1. Create the order in your database with status `pending`, using prices from your database.
2. Create the PaymentIntent or Checkout Session with the order ID in `metadata`, and save its ID on the order.
3. The customer pays.
4. The webhook finds the order by the ID in metadata and marks it `paid`.

This way every payment points to an order, and you never have a paid order you can't find. Abandoned `pending` orders can be cleaned up later.

## 102: What is a mandate?

A mandate is the customer's permission for you to debit their bank account or charge their payment method in the future. It's required for bank debits like SEPA Direct Debit and ACH, and for some card and local payment method setups in certain countries.

Stripe creates a Mandate object when the customer agrees in Checkout or the Payment Element, and shows the required legal text. You don't usually create mandates yourself, but your future payments rely on them.

## 103: What is the default payment method of a customer?

For subscriptions and invoices, Stripe uses `invoice_settings.default_payment_method` on the Customer, unless the subscription has its own `default_payment_method`.

```js
await stripe.customers.update("cus_123", {
  invoice_settings: { default_payment_method: "pm_123" },
});
```

If a customer adds a new card in your app, remember to make it the default, or their next renewal will still try the old card.

## 104: How do you save and remove payment methods for a customer?

Payment methods are attached to a customer when you confirm a SetupIntent or a PaymentIntent with `setup_future_usage` and a `customer`. You can also attach one directly:

```js
await stripe.paymentMethods.attach("pm_123", { customer: "cus_123" });
await stripe.paymentMethods.detach("pm_123");
```

Prefer SetupIntents for saving, because they run 3D Secure if needed. Attaching directly skips that, and later off-session payments may fail.

## 105: How do you list a customer's saved cards?

```js
const { data } = await stripe.customers.listPaymentMethods("cus_123", {
  type: "card",
});

for (const pm of data) {
  console.log(
    pm.card.brand,
    pm.card.last4,
    pm.card.exp_month,
    pm.card.exp_year,
  );
}
```

Show brand, last 4 digits and expiry, so the customer can recognize their cards. That is all the card data you get anyway.

## 106: What happens to saved cards when they expire or get replaced?

Card networks have updater services. When a bank issues a new card number or expiry date, Stripe can update the saved PaymentMethod automatically for supported cards. You get a `payment_method.automatically_updated` event.

This doesn't cover every card. For the rest, renewal payments fail and the customer must add a new card, usually through the Customer Portal or your billing page.

## 107: What information do you get about a card?

On `paymentMethod.card` you get things like `brand` (visa, mastercard...), `last4`, `exp_month`, `exp_year`, `country`, `funding` (credit, debit, prepaid), `fingerprint` and the results of `checks` (CVC, address, postal code).

You never get the full card number or the CVC. That data stays with Stripe.

## 108: What is a card fingerprint used for?

`card.fingerprint` is the same for the same card number within your account, even if the customer adds it several times. It's different for different cards.

You can use it to find duplicate cards on a customer, to limit free trials to one per card, or to spot a card used by many accounts, which can be a sign of fraud.

## 109: What are CVC and address checks?

When a card is used, the issuer can check the CVC and the billing address (AVS) and say whether they match. Stripe shows the result in `card.checks` as `pass`, `fail`, `unavailable` or `unchecked`.

A failed check doesn't always mean the payment fails. You can block on a failed CVC or postal code check with Radar rules. Some issuers decline by themselves when the CVC is wrong.

## 110: What is tokenization?

Tokenization means swapping sensitive data for a safe reference. The card number is sent to Stripe and you get back an ID like `pm_...`. The ID is useless to an attacker outside your Stripe account.

That's how Stripe keeps card data off your servers. Card networks have their own form of this too (network tokens), which Stripe can use behind the scenes to raise approval rates.

## 111: Why shouldn't you store card numbers yourself?

Storing card numbers puts your whole system in PCI scope: strict audits, network segmentation, encryption key management and a lot of paperwork. If you get breached, you face fines and loss of trust.

With Stripe you keep only IDs and safe details like brand and last 4 digits. Collect card data only with Stripe's components, and never log request bodies that could contain card data.

## 112: What is the hosted invoice page?

Every finalized invoice has a `hosted_invoice_url`, a Stripe-hosted page where the customer can see the invoice, download a PDF and pay it with the enabled payment methods. There is also `invoice_pdf` with a direct link to the PDF.

You can email the link yourself or let Stripe send it. It's handy for B2B invoices and for asking customers to fix a failed subscription payment.

## 113: What is the difference between charge_automatically and send_invoice?

These are the two values of `collection_method` on subscriptions and invoices:

- `charge_automatically`: Stripe charges the customer's saved payment method when the invoice is finalized. Typical for SaaS.
- `send_invoice`: Stripe emails the invoice and the customer pays it themselves before the due date (set with `days_until_due`). Typical for B2B with bank transfers.

## 114: What are price lookup keys?

A lookup key is your own name for a Price, like `pro_monthly`. You can fetch prices by it instead of hardcoding `price_...` IDs in your code:

```js
const { data } = await stripe.prices.list({ lookup_keys: ["pro_monthly"] });
```

When the price changes, you create a new Price and move the lookup key to it with `transfer_lookup_key: true`. Your code doesn't need to change, and IDs can differ between sandbox and live without config tricks.

## 115: Can you change or delete a Price?

You can't change the amount or interval of an existing Price. Prices are immutable, because existing subscriptions and invoices refer to them. You can change things like `nickname`, `metadata`, `lookup_key` and `active`.

To change a price, create a new Price and set the old one to `active: false` (archive it). Existing subscribers keep the old price until you move them.

## 116: What is tiered pricing?

Tiered pricing means the unit price depends on how many units are bought. Stripe supports two modes:

- `volume`: all units get the price of the tier the total falls into. 50 seats at $8 each.
- `graduated`: each tier is priced separately. The first 10 seats at $10, the next 40 at $8.

You set them with `billing_scheme: 'tiered'`, `tiers_mode` and a list of `tiers` on the Price.

## 117: How do you bill per seat?

Use a per-unit recurring Price and set the `quantity` on the subscription item to the number of seats:

```js
await stripe.subscriptions.update("sub_123", {
  items: [{ id: "si_123", quantity: 12 }],
  proration_behavior: "create_prorations",
});
```

When the team adds or removes users, update the quantity. Stripe prorates the change for the rest of the period.

## 118: What is usage-based billing?

Usage-based (metered) billing charges customers for what they actually used in a period, like API calls, GB stored or messages sent.

In Stripe you create a Meter that defines how to add up usage, connect a Price to it, and send meter events from your app as usage happens. At the end of the period, Stripe adds up the events and puts the amount on the invoice. The older usage records API was removed in the Basil release.

## 119: How does Checkout handle the Customer object?

If you pass `customer: 'cus_123'`, Checkout uses that customer and can show their saved details. If you don't, Checkout can create a customer for you. In subscription mode it always does, because subscriptions need one.

For one-time payments, set `customer_creation: 'always'` if you want a Customer for every buyer. Pass `customer_email` to pre-fill the email when you don't have a Customer yet.

## 120: How do you charge an amount that isn't a saved Price in Checkout?

Use `price_data` to define the price inline:

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price_data: {
        currency: "usd",
        unit_amount: 4999,
        product_data: { name: "Custom engraving" },
      },
      quantity: 1,
    },
  ],
  success_url: "https://example.com/success",
});
```

It's useful for carts with dynamic prices. The amount must still come from your server, not from the client.

## 121: What are the modes of a Checkout Session?

- `payment`: one-time payment.
- `subscription`: starts a subscription and takes the first payment (or starts a trial).
- `setup`: saves a payment method for later without charging.

The mode decides which other parameters you can use and which object Checkout creates: a PaymentIntent, a Subscription or a SetupIntent.

## 122: How long is a Checkout Session valid?

By default a Checkout Session expires 24 hours after it is created. You can set a shorter time with `expires_at` (at least 30 minutes from creation).

When it expires, Stripe sends `checkout.session.expired`. You can use that to release reserved stock or to send a "you left something in your cart" email if the customer agreed to that.

## 123: How do you show order details on the success page?

Read the `session_id` from the URL and retrieve the session on the server:

```js
const session = await stripe.checkout.sessions.retrieve(req.query.session_id, {
  expand: ["line_items"],
});

if (session.payment_status === "paid") {
  res.render("thanks", { email: session.customer_details.email });
}
```

Only show information; don't fulfill here. Also make sure the session belongs to the logged-in user if you show anything private.

## 124: What is embedded Checkout?

Embedded Checkout shows the Stripe Checkout form inside your page instead of redirecting to `checkout.stripe.com`. You create the session with the embedded UI mode, send its client secret to the front end, and mount it with Stripe.js.

The customer stays on your domain, but you still get Checkout's features. If you need even more control over the layout, Stripe also lets you use Checkout Sessions with your own Elements-based form.

## 125: How do you use Stripe in a React app?

Use `@stripe/react-stripe-js` together with `@stripe/stripe-js`:

```jsx
import { loadStripe } from "@stripe/stripe-js";
import {
  Elements,
  PaymentElement,
  useStripe,
  useElements,
} from "@stripe/react-stripe-js";

const stripePromise = loadStripe("pk_test_...");

function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  async function handleSubmit(e) {
    e.preventDefault();
    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: { return_url: `${window.location.origin}/complete` },
    });
    if (error) alert(error.message);
  }

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Pay</button>
    </form>
  );
}

export function Checkout({ clientSecret }) {
  return (
    <Elements stripe={stripePromise} options={{ clientSecret }}>
      <CheckoutForm />
    </Elements>
  );
}
```

Call `loadStripe` outside the component so it isn't recreated on every render.

## 126: How do mobile apps take payments with Stripe?

Stripe has SDKs for iOS, Android and React Native. They include a ready-made payment sheet (similar to the Payment Element) that supports cards, Apple Pay, Google Pay and other methods.

The back end works the same way: your server creates the PaymentIntent and returns its client secret, and the app shows the sheet and confirms. Note that app stores have their own rules about selling digital goods inside apps, which can affect whether you can use Stripe there.

## 127: What is Stripe Terminal?

Terminal is Stripe's product for in-person payments with physical card readers. Your app talks to the reader through the Terminal SDK, and the payments use the same PaymentIntents API as online payments.

This lets a business see online and in-store payments in one place, with the same customers, reports and payouts.

## 128: What is the difference between Stripe Payments and Stripe Billing?

Payments is about accepting single payments: PaymentIntents, Checkout, payment methods, refunds.

Billing is built on top and handles recurring revenue: Products and Prices, Subscriptions, Invoices, trials, prorations, usage-based billing, dunning and the Customer Portal. Billing has its own fee on top of payment fees.

## 129: How do you collect a customer's tax ID?

Customers can have tax IDs (like an EU VAT number). In Checkout, turn on tax ID collection, and the customer can enter it during payment. You can also add them with the API:

```js
await stripe.customers.createTaxId("cus_123", {
  type: "eu_vat",
  value: "DE123456789",
});
```

Tax IDs show on invoices, and Stripe Tax uses them for things like reverse charge in B2B sales in the EU.

## 130: How long does a refund take to reach the customer?

Stripe sends the refund to the bank right away, but it often takes 5 to 10 business days to show on the customer's statement, depending on the bank. Some banks show it faster.

Customers often ask "where is my refund?". You can give them the refund's ARN (acquirer reference number) when available, which their bank can use to trace it.

## 131: What statuses can a refund have?

A refund can be `pending`, `requires_action`, `succeeded`, `failed` or `canceled`. Most card refunds go to `succeeded` quickly.

A refund can fail, for example when the card was closed. Then the money goes back to your Stripe balance, and you have to pay the customer another way. Listen for `refund.updated` or `refund.failed` to catch this.

## 132: How do you cancel a PaymentIntent?

```js
await stripe.paymentIntents.cancel("pi_123", {
  cancellation_reason: "abandoned",
});
```

You can cancel a PaymentIntent before it succeeds, for example when the customer empties their cart. If it was authorized but not captured, canceling releases the hold on the customer's card. You can't cancel a succeeded payment. Refund it instead.

## 133: How should you store and use Stripe API keys in your app?

- Keep them in environment variables or a secret manager, not in code.
- Use different keys for local, staging and production.
- Use restricted keys for services that need limited access.
- Add `.env` to `.gitignore`, and add secret scanning to your repo.
- Never send the secret key to the browser or a mobile app.

Stripe also scans public GitHub repos for leaked keys, but don't rely on that.

## 134: What do you do if a secret key leaks?

Roll the key in the Dashboard right away. Stripe creates a new key, and you can let the old one keep working for a short time while you deploy the new one. Then check your logs and the Dashboard for requests you don't recognize.

After that, find out how it leaked (a commit, a log, a screenshot) and fix that, so it doesn't happen again.

## 135: How do webhook signatures work at a high level?

Stripe signs each event with your endpoint's secret, using HMAC-SHA256 over a timestamp and the raw request body. It sends the result in the `Stripe-Signature` header.

Your server does the same calculation with the same secret and compares. If they match, the event came from Stripe and wasn't changed. The SDK does this for you with `stripe.webhooks.constructEvent()`.

## 136: How are Stripe event types named?

Event types are the object type and what happened, separated by dots: `payment_intent.succeeded`, `customer.subscription.updated`, `invoice.payment_failed`, `charge.dispute.created`.

When you configure an endpoint, you pick the event types it receives. You can choose all events, but it's better to list only the ones your handler uses.

## 137: Do webhook events arrive in order?

No. Stripe doesn't guarantee the order. You might get `invoice.paid` before `invoice.created`, or an older `customer.subscription.updated` after a newer one.

Don't write code that depends on order. A good pattern is to treat each event as a hint that something changed, and fetch the current object from the API before updating your database.

## 138: Can the same webhook event arrive more than once?

Yes. If your server responds slowly or the network fails, Stripe may send the same event again. Your handler must be safe to run twice for the same event.

A simple way is to save each processed event ID in a table with a unique index, and skip events you have already handled.

## 139: What other Stripe CLI commands are useful?

- `stripe listen`: forward webhooks to your local server.
- `stripe trigger <event>`: create test objects that fire an event.
- `stripe logs tail`: watch your API request logs live.
- `stripe events resend <event_id>`: send an event again.
- `stripe customers create --email=a@b.com` (and other resources): call the API from the terminal.

It's a fast way to try API calls without writing code.

## 140: What is the livemode field?

Every object and event has `livemode: true` or `false`. `true` means it was created with live keys and real money. `false` means test data.

You can check it in your webhook handler as an extra safety check, for example to make sure a staging server never processes live events by mistake.

## 141: How does the Stripe API accept parameters?

The v1 API takes form-encoded request bodies (`application/x-www-form-urlencoded`) and returns JSON. Nested fields use brackets, like `metadata[orderId]=123`.

```bash
curl https://api.stripe.com/v1/customers \
  -u sk_test_123: \
  -d email=ana@example.com \
  -d "metadata[userId]=42"
```

The SDKs hide this and let you pass normal objects. The newer v2 endpoints use JSON request bodies.

## 142: What is an invoice item?

An invoice item is a one-off line you add to a customer's invoice, for example a setup fee or extra usage. If you create one without an invoice, it waits and gets added to the customer's next invoice, for example the next subscription renewal.

```js
await stripe.invoiceItems.create({
  customer: "cus_123",
  amount: 5000,
  currency: "usd",
  description: "Onboarding fee",
});
```

## 143: How do you change the payout schedule?

Payouts are automatic by default, with a schedule depending on your country (often daily). In the Dashboard you can set them to daily, weekly or monthly, or switch to manual payouts and create them with the API.

Manual payouts are useful when you want to control cash timing, but they add work. For most businesses, automatic payouts are simpler.

## 144: What is a Quote in Stripe?

A Quote is a price proposal you send to a customer before they buy, common in B2B sales. It lists products, prices and discounts. When the customer accepts it, Stripe can turn it into an invoice or a subscription.

It saves you from building your own quote documents and then copying the details into Stripe by hand.

## 145: Should you use the Stripe Customer ID as your user ID?

No. Keep your own user ID as the main key and store the Stripe Customer ID as a separate column. Your app should work even if the Stripe customer is recreated, or if you have different Stripe accounts for different regions.

Also put your user ID in the Customer's `metadata`, so you can go both ways when debugging.

## 146: What happens if you create a new Stripe customer on every checkout?

The same person ends up as many customers in Stripe. Their saved cards, invoices and subscriptions are split up, the Customer Portal shows only part of their history, and reporting gets messy.

Create the Stripe Customer once, store its ID on your user, and pass it to every Checkout Session or PaymentIntent for that user.

## 147: What is a payment method's billing details field?

`billing_details` on a PaymentMethod holds the name, email, phone and address the customer gave when paying. It's used for address checks, receipts and some payment methods that need an address.

It isn't the same as the Customer's address or shipping address, so don't mix them up when you build invoices or ship goods.

## 148: What is shipping address collection in Checkout?

Checkout can ask for a shipping address. You set which countries you ship to:

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [{ price: "price_123", quantity: 1 }],
  shipping_address_collection: { allowed_countries: ["US", "CA"] },
  success_url: "https://example.com/success",
});
```

You can also offer shipping rates (standard, express) with `shipping_options`. The address is then available on the completed session in your webhook.

## 149: What is the minimum amount you can charge?

Stripe has a minimum per charge that depends on the currency, for example $0.50 for USD. If you try less, the API returns an error.

This matters for things like small tips or usage charges. You might need to group small amounts together, or use a $0 flow (like a SetupIntent or a trial) when you only want to save a card.

## 150: Where can you see why a payment failed?

- In the Dashboard, open the payment. It shows the decline code, the Radar risk evaluation and the timeline.
- In the API, look at `last_payment_error` on the PaymentIntent, and `outcome` on the Charge (`outcome.type`, `outcome.reason`, `outcome.risk_level`).
- In the `payment_intent.payment_failed` webhook, which has the same data.

These tell you whether it was the bank, Radar or a problem in your request.

# Moderate Questions (151-300)

## 151: How do you build a basic PaymentIntent endpoint on the server?

The client sends what it wants to buy, the server calculates the amount and returns the client secret:

```js
import express from "express";
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
const app = express();

app.post("/api/payment-intents", express.json(), async (req, res) => {
  const order = await orders.createPending(req.user.id, req.body.items); // prices from your DB

  const pi = await stripe.paymentIntents.create(
    {
      amount: order.totalCents,
      currency: "usd",
      customer: req.user.stripeCustomerId,
      metadata: { orderId: order.id },
    },
    { idempotencyKey: `order-${order.id}-pi` },
  );

  await orders.setPaymentIntent(order.id, pi.id);
  res.json({ clientSecret: pi.client_secret });
});
```

The front end then mounts the Payment Element with this client secret and calls `stripe.confirmPayment()`.

## 152: What is deferred intent creation?

In the deferred flow you show the Payment Element before any PaymentIntent exists. You create Elements with the amount and currency, and only create the PaymentIntent when the customer clicks "Pay":

```js
const elements = stripe.elements({
  mode: "payment",
  amount: 2000,
  currency: "usd",
});
elements.create("payment").mount("#payment-element");

async function pay() {
  const { error: submitError } = await elements.submit(); // validate the form
  if (submitError) return show(submitError.message);

  const { clientSecret } = await fetch("/api/payment-intents", {
    method: "POST",
  }).then((r) => r.json());

  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: { return_url: "https://example.com/complete" },
  });
  if (error) show(error.message);
}
```

This avoids creating many unused PaymentIntents for visitors who never pay, and lets the final amount depend on what the customer picks on the page.

## 153: What are confirmation tokens?

A ConfirmationToken holds the payment details the customer entered in Elements, so your server can look at them before confirming the payment. The client creates it, sends its ID to the server, and the server confirms the PaymentIntent with it.

```js
// client
const { confirmationToken, error } = await stripe.createConfirmationToken({
  elements,
});

// server
await stripe.paymentIntents.create({
  amount: 2000,
  currency: "usd",
  confirm: true,
  confirmation_token: req.body.confirmationTokenId,
  return_url: "https://example.com/complete",
});
```

It's useful when the server must decide something based on the payment method, like adding a fee for some methods or running extra checks, before charging.

## 154: How do you verify Stripe webhooks in Express?

Use the raw body for this route and let the SDK check the signature:

```js
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  async (req, res) => {
    let event;
    try {
      event = stripe.webhooks.constructEvent(
        req.body, // a Buffer, not parsed JSON
        req.headers["stripe-signature"],
        process.env.STRIPE_WEBHOOK_SECRET,
      );
    } catch (err) {
      return res.status(400).send(`Webhook error: ${err.message}`);
    }

    await handleEvent(event);
    res.sendStatus(200);
  },
);
```

Register this route before any global `express.json()` middleware, or make sure that middleware skips it.

## 155: Why does webhook signature verification need the raw body?

The signature is computed over the exact bytes Stripe sent. If a JSON parser reads the body and you turn it back into a string, the result can differ: other spacing, key order or number formatting. Then the signature doesn't match, and verification fails.

This is the most common webhook bug. The fix is always to give `constructEvent()` the raw body, as a Buffer or the original string.

## 156: How do you handle Stripe webhooks in a Next.js route handler?

Read the body as text, which keeps it raw:

```js
// app/api/webhooks/stripe/route.js
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function POST(request) {
  const body = await request.text();
  const signature = request.headers.get("stripe-signature");

  let event;
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET,
    );
  } catch {
    return new Response("Invalid signature", { status: 400 });
  }

  await handleEvent(event);
  return new Response(null, { status: 200 });
}
```

Don't call `request.json()` first. The body can only be read once.

## 157: How do you make a webhook handler idempotent?

Record each event ID and skip ones you've already processed. Doing the record and the work in one database transaction keeps them consistent:

```js
async function handleEvent(event) {
  await db.transaction(async (tx) => {
    const inserted = await tx.query(
      "INSERT INTO stripe_events (id, type) VALUES ($1, $2) ON CONFLICT (id) DO NOTHING RETURNING id",
      [event.id, event.type],
    );
    if (inserted.rowCount === 0) return; // already handled

    if (event.type === "checkout.session.completed") {
      await markOrderPaid(tx, event.data.object.metadata.orderId);
    }
  });
}
```

Also make the actions themselves safe to repeat, for example "set order status to paid" instead of "add one to paid orders".

## 158: Why process webhooks in a background queue?

Stripe expects a quick 2xx response. If your handler sends emails, calls other APIs or does heavy database work, it can time out, and Stripe will retry, which creates duplicates and load.

A common setup: the endpoint verifies the signature, stores the event (or pushes it to a queue like SQS, BullMQ or RabbitMQ) and returns 200. Workers then process events with their own retries, and failed ones go to a dead letter queue you can inspect.

## 159: How do you deal with webhook events arriving out of order?

Don't trust the event's copy of the object to be the latest. When you get an event, fetch the current object from Stripe and save that:

```js
if (event.type.startsWith("customer.subscription.")) {
  const sub = await stripe.subscriptions.retrieve(event.data.object.id);
  await saveSubscription(sub); // always the current state
}
```

Now it doesn't matter which event comes first, the database ends up with the latest state. This costs an API call per event, which is usually fine. Don't compare `created` timestamps to order events, because they only have one second precision.

## 160: What is the difference between thin events and snapshot events?

Snapshot events are the classic format. The event includes a full copy of the object as it was when the event happened (`data.object`), plus `previous_attributes` for updates.

Thin events are smaller. They include the event type and a reference to the related object, but not the object itself. Your code fetches the object (or the full event) when it needs it, so you always work with current data and the payload doesn't depend on an API version. Stripe recommends thin events for new integrations, and the v2 APIs only use them. Thin and snapshot events need separate destinations.

## 161: What are event destinations?

Event destinations are the newer name for where Stripe sends events. A destination can be a webhook endpoint (your HTTPS URL) or a cloud service like Amazon EventBridge.

For each destination you choose the event types, the payload format (thin or snapshot), the API version and the scope: your own account, your connected accounts or other accounts in your organization. Stripe limits how many destinations one account can have, so don't create one per feature.

## 162: How does Stripe retry failed webhook deliveries?

In live mode, Stripe retries a failed delivery with exponential backoff for up to three days. In sandboxes it retries only a few times over a few hours. A delivery fails if your server returns a non-2xx status, times out or redirects.

You can resend events by hand from the Dashboard (up to 15 days after the event) or with the Stripe CLI (up to 30 days). If an endpoint keeps failing for a long time, Stripe emails you and may disable it.

## 163: Why does the API version of a webhook endpoint matter?

Snapshot events are rendered with the API version of the endpoint (or your account default), fixed when the event is created. If your SDK and its types use a newer version than the endpoint, the event objects can have a different shape than your code expects.

Create the endpoint with the same API version your SDK is pinned to, and when you upgrade, plan the change for both. Thin events avoid much of this problem because you fetch the object with your own version.

## 164: How do you choose idempotency keys?

The key should identify one business operation, so a retry of the same operation uses the same key, and a new operation uses a new key. Good examples:

- `order-123-create-payment-intent`
- `refund-request-456` (your own refund request ID)
- `invoice-789-retry-2`

A random UUID works only if you generate it once and store it, then reuse it on retries. Generating a new UUID on each retry gives no protection. Keys can be up to 255 characters.

## 165: What happens if you reuse an idempotency key with different parameters?

Stripe compares the new request with the first one. If the parameters differ, it returns an idempotency error instead of running the request. This protects you from bugs where two different operations share a key.

Keys are kept for at least 24 hours. After that, the same key is treated as new. Also, if the first request failed validation before it started (for example a missing parameter), the key is not saved, so you can fix the request and retry with the same key.

## 166: Does the Node SDK retry requests by itself?

Yes. The SDK retries failed network requests and some server errors with backoff. The `maxNetworkRetries` setting controls how many times (set it to 0 to turn it off). On retries of `POST` requests the SDK adds an idempotency key for you, so a retry doesn't create a second object.

```js
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  maxNetworkRetries: 2,
  timeout: 20_000,
});
```

Your own retries (for example in a job queue) still need your own idempotency keys, because they are new requests from the SDK's point of view.

## 167: How do you handle Stripe errors in code?

Check the error class and react to each kind:

```js
try {
  await stripe.paymentIntents.confirm("pi_123", { payment_method: "pm_123" });
} catch (err) {
  if (err instanceof Stripe.errors.StripeCardError) {
    return { userMessage: err.message, declineCode: err.decline_code };
  }
  if (err instanceof Stripe.errors.StripeRateLimitError) {
    return retryLater();
  }
  if (err instanceof Stripe.errors.StripeConnectionError) {
    // unknown outcome: check the PaymentIntent status before trying again
    return reconcileLater("pi_123");
  }
  logger.error({ requestId: err.requestId, code: err.code }, "stripe error");
  throw err;
}
```

Show card error messages to the user. For the rest, show a generic message and log the details.

## 168: How do you handle 3D Secure when you confirm on the server?

If you confirm the PaymentIntent on the server, it may end in `requires_action`. Send the client secret back to the browser and let Stripe.js handle the next step:

```js
// client
const { clientSecret, status } = await fetch("/api/pay", {
  method: "POST",
}).then((r) => r.json());

if (status === "requires_action") {
  const { error, paymentIntent } = await stripe.handleNextAction({
    clientSecret,
  });
  if (error) show(error.message);
  else if (paymentIntent.status === "succeeded") showSuccess();
}
```

With client-side confirmation (`stripe.confirmPayment()`), Stripe.js handles this for you.

## 169: How do you charge a saved card when the customer isn't present?

Create and confirm a PaymentIntent with `off_session: true`:

```js
try {
  await stripe.paymentIntents.create({
    amount: 4900,
    currency: "usd",
    customer: "cus_123",
    payment_method: "pm_123",
    off_session: true,
    confirm: true,
  });
} catch (err) {
  if (err.code === "authentication_required") {
    // the bank wants the customer to authenticate
    await notifyCustomerToComplete(err.raw.payment_intent.id);
  } else {
    throw err;
  }
}
```

If authentication is needed, bring the customer back to your site (email or in-app message) and confirm the same PaymentIntent on-session.

## 170: How do you save a card with a SetupIntent?

Server:

```js
const setupIntent = await stripe.setupIntents.create({
  customer: "cus_123",
  usage: "off_session",
});
res.json({ clientSecret: setupIntent.client_secret });
```

Client:

```js
const elements = stripe.elements({ clientSecret });
elements.create("payment").mount("#payment-element");

const { error } = await stripe.confirmSetup({
  elements,
  confirmParams: { return_url: "https://example.com/billing" },
});
```

When it succeeds, the PaymentMethod is attached to the customer and you get `setup_intent.succeeded`. Set it as the default payment method if this is the card for renewals.

## 171: How do you authorize now and capture later?

Create the PaymentIntent with `capture_method: 'manual'`. After confirmation, its status is `requires_capture`. Capture when you're ready:

```js
const pi = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "cus_123",
  capture_method: "manual",
});

// later, for example when the order ships
await stripe.paymentIntents.capture(pi.id, { amount_to_capture: 8500 });
```

You can capture less than authorized, and the rest of the hold is released. To cancel, call `paymentIntents.cancel()`.

## 172: How long does an authorization last, and can it be extended?

For most online card payments you must capture within 7 days, or the authorization expires and the PaymentIntent is canceled. Other payment methods have their own limits.

Some card types and merchant categories support extended authorization (longer holds) and incremental authorization (raising the held amount, for example in hotels). These depend on the card network and need to be requested when you create the PaymentIntent.

## 173: How do you connect refunds to your own data?

Add your IDs in the refund's `metadata`, and use an idempotency key based on your own refund request:

```js
await stripe.refunds.create(
  {
    payment_intent: order.paymentIntentId,
    amount: 1500,
    reason: "requested_by_customer",
    metadata: { orderId: order.id, refundRequestId: request.id },
  },
  { idempotencyKey: `refund-${request.id}` },
);
```

Then update your order when you get the refund webhook, not only when the API call returns, because refunds can fail later.

## 174: How do you create a subscription with a custom payment form?

Create the subscription with `payment_behavior: 'default_incomplete'`, so it waits for the first payment, and send the client secret of the first invoice to the client:

```js
const subscription = await stripe.subscriptions.create({
  customer: "cus_123",
  items: [{ price: "price_pro_monthly" }],
  payment_behavior: "default_incomplete",
  payment_settings: { save_default_payment_method: "on_subscription" },
  expand: ["latest_invoice.confirmation_secret"],
});

res.json({
  subscriptionId: subscription.id,
  clientSecret: subscription.latest_invoice.confirmation_secret.client_secret,
});
```

The client confirms with the Payment Element. Until then the subscription is `incomplete`. If you don't need a custom form, Checkout in `subscription` mode does all of this for you.

## 175: What changed about invoices and PaymentIntents in the Basil release?

In the Basil release (`2025-03-31.basil`), Stripe removed several fields from the Invoice object, including `payment_intent`, `charge`, `paid` and `subscription`. An invoice can now be paid by several payments, so a single `payment_intent` field no longer made sense.

Now you use the invoice's payments list (invoice payments) to see the PaymentIntents, `confirmation_secret` to get a client secret for confirming, and `parent.subscription_details.subscription` to find the subscription. Older blog posts and Stack Overflow answers often use the removed fields.

## 176: Where do you find the current billing period of a subscription now?

Since Basil, `current_period_start` and `current_period_end` are on each subscription item, not on the subscription:

```js
const sub = await stripe.subscriptions.retrieve("sub_123");
const periodEnd = sub.items.data[0].current_period_end; // Unix seconds
```

This allows items with different billing periods in one subscription. Code that reads `subscription.current_period_end` breaks after upgrading to a Basil or newer API version.

## 177: Which events should you use to give and remove subscription access?

A common approach:

- `invoice.paid`: a period was paid, give or extend access.
- `customer.subscription.updated`: status or plan changed, sync your copy.
- `customer.subscription.deleted`: the subscription ended, remove access.
- `invoice.payment_failed`: tell the customer to update their payment method.

Instead of handling each one differently, many apps fetch the subscription on each of these events and set access from its status. Fewer code paths means fewer bugs.

## 178: What happens when a subscription renewal payment fails?

The invoice stays `open`, the subscription goes to `past_due`, and you get `invoice.payment_failed`. Stripe then retries the payment based on your settings (for example Smart Retries over a couple of weeks) and can email the customer.

If a retry works, the invoice becomes `paid` and the subscription `active` again. If all retries fail, Stripe does what you configured: cancel the subscription, mark it `unpaid`, or leave it `past_due`. Your app should decide how long to keep access during this time.

## 179: What are Smart Retries and dunning?

Dunning is the process of collecting failed recurring payments: retrying the charge and reminding the customer. Smart Retries is Stripe's feature that picks retry times based on what is most likely to work for that card and bank, instead of a fixed schedule.

You set the retry window, the reminder emails and the final action in the Billing settings. Good dunning recovers a big part of failed payments without any code from you.

## 180: How do you upgrade a plan and charge the difference right away?

Use `proration_behavior: 'always_invoice'`:

```js
await stripe.subscriptions.update("sub_123", {
  items: [{ id: "si_123", price: "price_business_monthly" }],
  proration_behavior: "always_invoice",
  payment_behavior: "pending_if_incomplete",
});
```

With `always_invoice` Stripe creates an invoice for the prorated amount now, instead of adding it to the next renewal. `pending_if_incomplete` keeps the old plan active until the upgrade payment succeeds, so customers can't get the better plan if the charge fails.

## 181: How do you show the customer what a plan change will cost before they confirm?

Create a preview invoice:

```js
const preview = await stripe.invoices.createPreview({
  customer: "cus_123",
  subscription: "sub_123",
  subscription_details: {
    items: [{ id: "si_123", price: "price_business_monthly" }],
    proration_behavior: "create_prorations",
  },
});

console.log(preview.amount_due);
```

The preview isn't saved and doesn't charge anything. It replaced the old "upcoming invoice" endpoints, which were removed in the Basil release.

## 182: How do you downgrade at the end of the billing period?

If you just update the price, the change happens now. For "downgrade next month", use a subscription schedule with two phases: the current plan until the period end, then the new plan.

```js
const schedule = await stripe.subscriptionSchedules.create({
  from_subscription: "sub_123",
});
const current = schedule.phases[0];

await stripe.subscriptionSchedules.update(schedule.id, {
  phases: [
    {
      items: current.items.map((i) => ({
        price: i.price,
        quantity: i.quantity,
      })),
      start_date: current.start_date,
      end_date: current.end_date,
    },
    { items: [{ price: "price_basic_monthly", quantity: 1 }] },
  ],
});
```

Some teams store the pending downgrade in their own database instead and apply it on the renewal event. Schedules are cleaner but have more rules to learn.

## 183: What are subscription schedules used for?

A subscription schedule describes how a subscription changes over time as a list of phases. Each phase has its own prices, quantities, discounts or trial.

Use cases: a downgrade at period end, an intro price for 3 months then the normal price, a contract that starts on a future date, or a yearly contract with a price increase after the first year. While a schedule controls a subscription, change it through the schedule, not by updating the subscription directly.

## 184: How do you cancel immediately and refund the unused time?

`stripe.subscriptions.cancel()` accepts `prorate` and `invoice_now`:

```js
await stripe.subscriptions.cancel("sub_123", {
  prorate: true,
  invoice_now: true,
});
```

This creates a final invoice with a credit for the unused time. The credit goes to the customer's credit balance, not to their card. If you want to return money to the card, create a refund for the right amount yourself, or issue a credit note with a refund.

## 185: How do you pause a subscription?

One way is `pause_collection`, which keeps the subscription but changes what happens to its invoices:

```js
await stripe.subscriptions.update("sub_123", {
  pause_collection: { behavior: "void" }, // or 'keep_as_draft', 'mark_uncollectible'
});
```

`void` is the usual choice for "pause my membership", because no invoices are collected. Set `pause_collection` to an empty value to resume. Newer API versions also have a dedicated pause action for subscriptions, and the Customer Portal can let customers pause on their own.

## 186: How do you offer a free trial without asking for a card?

In Checkout, set `payment_method_collection: 'if_required'` with a trial. For subscriptions created by the API, just don't require a payment method. Then decide what happens if the trial ends with no card:

```js
await stripe.subscriptions.create({
  customer: "cus_123",
  items: [{ price: "price_pro_monthly" }],
  trial_period_days: 14,
  trial_settings: {
    end_behavior: { missing_payment_method: "cancel" }, // or 'pause', 'create_invoice'
  },
});
```

No-card trials get more sign-ups but fewer paid conversions. Remind customers to add a card when you get `customer.subscription.trial_will_end`.

## 187: How do you set up metered billing with meters?

Create a meter, a price that uses it, a subscription with that price, and then send usage events:

```js
const meter = await stripe.billing.meters.create({
  display_name: "API requests",
  event_name: "api_requests",
  default_aggregation: { formula: "sum" },
});

const price = await stripe.prices.create({
  product: "prod_api",
  currency: "usd",
  unit_amount_decimal: "0.1", // $0.001 per request, in cents
  recurring: { interval: "month", usage_type: "metered", meter: meter.id },
});

await stripe.billing.meterEvents.create({
  event_name: "api_requests",
  payload: { stripe_customer_id: "cus_123", value: "25" },
  identifier: "req-batch-2026-11-19-0001", // for deduplication
});
```

At the end of the period, Stripe adds up the events for each customer and bills them.

## 188: What is the Entitlements API?

Entitlements connect products to features in your app. You define features (like `advanced_reports`) and attach them to products. When a customer has an active subscription to that product, Stripe lists the feature in their active entitlements.

```js
const { data } = await stripe.entitlements.activeEntitlements.list({
  customer: "cus_123",
});
const features = data.map((e) => e.lookup_key);
```

You get an event when a customer's entitlements change, so you can update a cached copy. It saves you from writing your own "which plan gets which feature" mapping.

## 189: How do you send a customer to the Customer Portal?

Create a portal session and redirect:

```js
app.post("/billing/portal", async (req, res) => {
  const session = await stripe.billingPortal.sessions.create({
    customer: req.user.stripeCustomerId,
    return_url: "https://example.com/account",
  });
  res.redirect(303, session.url);
});
```

The session link is short-lived and logs the customer in to their own billing, so only create it for the logged-in user's own Stripe customer. Never take the customer ID from the request body.

## 190: How do you keep subscription data in your database in sync with Stripe?

- Store the subscription ID, status, price, quantity and period end in your table.
- Update it from webhooks (`customer.subscription.*`, `invoice.paid`), fetching the latest subscription each time.
- Use one function, like `syncSubscription(subId)`, that all events call.
- Run a periodic job that compares your table to Stripe and fixes differences, in case a webhook was missed.

Your app then reads its own table on each request, which is fast and doesn't use Stripe's rate limit.

## 191: How do you create a subscription with Checkout?

```js
const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  customer: user.stripeCustomerId,
  line_items: [{ price: "price_pro_monthly", quantity: 1 }],
  subscription_data: {
    trial_period_days: 14,
    metadata: { userId: user.id },
  },
  success_url: "https://example.com/welcome?session_id={CHECKOUT_SESSION_ID}",
  cancel_url: "https://example.com/pricing",
});
```

In the `checkout.session.completed` webhook, read `session.subscription` and save it for the user.

## 192: Where should metadata go when you use Checkout?

Metadata on the Checkout Session stays on the session only. If you also want it on the objects Checkout creates, set it there too:

- `payment_intent_data.metadata`: copied to the PaymentIntent (payment mode).
- `subscription_data.metadata`: copied to the Subscription (subscription mode).
- `setup_intent_data.metadata`: copied to the SetupIntent (setup mode).

This matters because later events, like `invoice.paid` or `charge.refunded`, are about those objects, not the session. If the metadata isn't on them, your handler can't find your order or user.

## 193: What is client_reference_id in Checkout?

It's a field where you put your own ID for this checkout, like a cart ID or user ID. It comes back on the completed session.

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  client_reference_id: cart.id,
  line_items: cart.lineItems,
  success_url: "https://example.com/success",
});
```

It's similar to metadata but only one value and only on the session. It's handy with Payment Links too, where you can add it as a URL parameter.

## 194: How do you write a safe fulfillment function for Checkout?

Make one function that can be called from the webhook and the success page, and that is safe to run many times:

```js
async function fulfillCheckout(sessionId) {
  const session = await stripe.checkout.sessions.retrieve(sessionId, {
    expand: ["line_items"],
  });
  if (session.payment_status === "unpaid") return; // wait for async payment

  await db.transaction(async (tx) => {
    const order = await tx.orders.lockBySessionId(sessionId); // SELECT ... FOR UPDATE
    if (order.status === "fulfilled") return;
    await tx.orders.markFulfilled(order.id, session.line_items.data);
  });
}
```

The lock and the status check make sure the order is fulfilled once, even if the webhook and the success page call it at the same time.

## 195: How can you recover abandoned Checkout sessions?

Checkout can create a recovery link when a session expires. Turn it on when you create the session:

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [{ price: "price_123", quantity: 1 }],
  after_expiration: { recovery: { enabled: true } },
  consent_collection: { promotions: "auto" },
  success_url: "https://example.com/success",
});
```

In the `checkout.session.expired` event, the session has a recovery URL. You can email it to customers who agreed to receive marketing emails.

## 196: How do you style the Payment Element?

Use the Appearance API when you create Elements:

```js
const elements = stripe.elements({
  clientSecret,
  appearance: {
    theme: "flat",
    variables: {
      colorPrimary: "#0a7cff",
      borderRadius: "6px",
      fontFamily: "Inter, system-ui, sans-serif",
    },
    rules: {
      ".Input": { border: "1px solid #ccc" },
    },
  },
});
```

You can't style the iframe with your own CSS, because it lives on Stripe's domain. Themes, variables and rules cover most design needs.

## 197: What is the Express Checkout Element?

It shows one-click payment buttons like Apple Pay, Google Pay, Link and PayPal (when enabled), usually at the top of a product or cart page. The customer can pay without filling a form.

```js
const expressCheckout = elements.create("expressCheckout");
expressCheckout.mount("#express-checkout");

expressCheckout.on("confirm", async () => {
  const { clientSecret } = await createPaymentIntentOnServer();
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: { return_url: "https://example.com/complete" },
  });
  if (error) show(error.message);
});
```

It's often used together with the Payment Element further down the page.

## 198: How do you register payment method domains with the API?

```js
await stripe.paymentMethodDomains.create({ domain_name: "shop.example.com" });
```

Each domain and subdomain where wallets appear needs to be registered, including staging domains if you want to test wallets there. On Connect, register domains for connected accounts too when payments run on their accounts.

## 199: When should you create the Stripe Customer for a user?

Two common options:

- On sign-up: every user has a customer, which is simple, but you create many customers who never pay.
- Lazily, on the first checkout: fewer unused customers, but you must avoid creating two customers if the user clicks twice.

For the lazy way, use your user ID in the idempotency key and save the customer ID with a check:

```js
async function getOrCreateCustomer(user) {
  if (user.stripeCustomerId) return user.stripeCustomerId;
  const customer = await stripe.customers.create(
    { email: user.email, metadata: { userId: user.id } },
    { idempotencyKey: `customer-for-user-${user.id}` },
  );
  await db.users.setStripeCustomerIdIfEmpty(user.id, customer.id);
  return (await db.users.find(user.id)).stripeCustomerId;
}
```

## 200: Why shouldn't you look up customers by email with the Search API during checkout?

Search is eventually consistent. A customer created a few seconds ago may not show up yet, so you'll create a duplicate. Emails also aren't unique in Stripe, and users can change them.

Store the Stripe Customer ID on your user record and look it up there. Use search for admin tools and debugging, not for core payment logic.

## 201: How do you expand fields on list results?

On list calls, prefix the field with `data.`:

```js
const invoices = await stripe.invoices.list({
  customer: "cus_123",
  limit: 20,
  expand: ["data.customer"],
});
```

Expanding on lists makes each response bigger and slower, so expand only what you use. Stripe also has limits on how deep you can expand.

## 202: How do you upgrade to a new Stripe API version safely?

1. Read the changelog for every version between yours and the target, especially the major release notes (like Basil or Endive).
2. Search your code for the fields and parameters that changed.
3. Upgrade the SDK in a branch, since the SDK pins its own API version. TypeScript errors will point to many of the changes.
4. Test in a sandbox, including webhooks, using a new endpoint with the new version.
5. Deploy the code, then switch webhook endpoints to the new version.

Inside a major release, the monthly versions don't have breaking changes, so you can move between them more freely.

## 203: How does the Node SDK decide which API version to use?

Each SDK release is pinned to the API version that was current when it came out, and its TypeScript types describe that version. You can set another version when you create the client, or per request:

```js
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  apiVersion: "2026-09-30.endive",
});
```

If you set a different version than the SDK's own, the types may not match the real responses. It's usually better to upgrade the SDK and the version together.

## 204: How do you unit test code that calls Stripe?

Put Stripe calls behind your own small module (like `payments.createIntentForOrder()`) and mock that module in unit tests. Then you test your logic, not Stripe.

For tests closer to the real API, `stripe-mock` is an open source mock server that returns valid fake responses based on Stripe's OpenAPI spec. You point the SDK at it with the `host`, `port` and `protocol` options. It doesn't keep state, so it's good for "is my request valid" tests, not for full flows.

## 205: How do you run integration tests against Stripe?

Use a sandbox with its own test keys. Create real test objects with test payment methods:

```js
const pi = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method: "pm_card_visa",
  confirm: true,
  return_url: "https://example.com/return", // needed if a redirect method could be used
});
expect(pi.status).toBe("succeeded");
```

Run these in a separate, slower test suite, not on every save. Keep an eye on sandbox rate limits, which are lower than live ones.

## 206: How do you test your webhook handler without Stripe sending events?

Build a signed payload with `generateTestHeaderString`, then call your endpoint like Stripe would:

```js
const payload = JSON.stringify({
  id: "evt_test_1",
  object: "event",
  type: "checkout.session.completed",
  data: {
    object: {
      id: "cs_test_1",
      payment_status: "paid",
      metadata: { orderId: "42" },
    },
  },
});

const header = stripe.webhooks.generateTestHeaderString({
  payload,
  secret: process.env.STRIPE_WEBHOOK_SECRET,
});

await request(app)
  .post("/webhooks/stripe")
  .set("stripe-signature", header)
  .set("content-type", "application/json")
  .send(payload)
  .expect(200);
```

This tests signature checking, routing and your logic. Also test a wrong signature and a duplicate event.

## 207: How do you test a subscription renewal with test clocks?

Create a clock, a customer on that clock and a subscription, then advance the clock past the period end:

```js
const clock = await stripe.testHelpers.testClocks.create({ frozen_time: now });
const customer = await stripe.customers.create({
  test_clock: clock.id,
  payment_method: "pm_card_visa",
  invoice_settings: { default_payment_method: "pm_card_visa" },
});
await stripe.subscriptions.create({
  customer: customer.id,
  items: [{ price: "price_monthly" }],
});

await stripe.testHelpers.testClocks.advance(clock.id, {
  frozen_time: now + 32 * 24 * 60 * 60,
});
```

Advancing takes a little time, and the clock's status shows when it's ready. Your webhook endpoint receives the renewal events just like in real life. To test failed renewals, switch the default payment method to a declining test card before advancing.

## 208: What are the charge types in Stripe Connect?

- Direct charges: the payment is created on the connected account. The connected account is the merchant, pays Stripe's fees and handles refunds and disputes. The platform can take an application fee.
- Destination charges: the payment is created on the platform, and part of it is moved to one connected account automatically. The platform pays fees and is responsible for refunds and disputes.
- Separate charges and transfers: the platform charges the customer, then sends transfers to one or more connected accounts later. The most flexible option, for example to split one payment among several sellers.

## 209: How do you create a destination charge?

```js
const pi = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  application_fee_amount: 1500,
  transfer_data: { destination: "acct_seller123" },
  metadata: { orderId: "order_42" },
});
```

The customer pays the platform, Stripe moves $100 minus the $15 application fee to the seller, and the platform pays Stripe's fees out of its share. Instead of an application fee, you can set `transfer_data.amount` to say exactly how much the seller gets.

## 210: How do you create a direct charge?

Make the request as the connected account with the `stripeAccount` option:

```js
const pi = await stripe.paymentIntents.create(
  {
    amount: 10000,
    currency: "usd",
    application_fee_amount: 500,
  },
  { stripeAccount: "acct_business123" },
);
```

The PaymentIntent lives on the connected account. On the front end, initialize Stripe.js with the same account (`loadStripe(pk, { stripeAccount })`), or confirmation fails because the PaymentIntent can't be found.

## 211: How do you use separate charges and transfers?

Charge on the platform, then move money with transfers. Use `transfer_group` to link them, and `source_transaction` to tie each transfer to the charge so it doesn't fail while funds are still pending:

```js
const pi = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  transfer_group: "order_42",
});

// after payment_intent.succeeded
await stripe.transfers.create({
  amount: 6000,
  currency: "usd",
  destination: "acct_sellerA",
  transfer_group: "order_42",
  source_transaction: chargeId,
});
await stripe.transfers.create({
  amount: 2500,
  currency: "usd",
  destination: "acct_sellerB",
  transfer_group: "order_42",
  source_transaction: chargeId,
});
```

The platform keeps what's left ($15 here) and pays the Stripe fees.

## 212: What does on_behalf_of do?

`on_behalf_of` makes the connected account the merchant of record for a payment, even though the payment is created on the platform. The connected account's country and settings are used for the statement descriptor, settlement and fees.

It's often used with destination charges when the platform and the connected accounts are in different countries, so customers see the seller's name and the payment settles in the right country.

## 213: How do you know when a connected account can accept payments and get payouts?

Check `charges_enabled`, `payouts_enabled` and `requirements` on the account, and listen for `account.updated`:

```js
if (event.type === "account.updated") {
  const account = event.data.object;
  await sellers.update(account.id, {
    canSell: account.charges_enabled,
    canGetPaid: account.payouts_enabled,
    missing: account.requirements.currently_due,
  });
}
```

`requirements.currently_due` lists what Stripe still needs. If it's not empty, send the user back to onboarding with a new Account Link.

## 214: How do Connect webhooks differ from normal webhooks?

Events that happen on connected accounts (like a direct charge succeeding) are only sent to destinations set up to receive events from connected accounts. These events have an `account` field with the connected account ID.

```js
if (event.account) {
  // event from a connected account
  await handleConnectedEvent(event.account, event);
}
```

To fetch related objects, pass `{ stripeAccount: event.account }`, because the objects live on that account. Locally, use `stripe listen --forward-connect-to`.

## 215: How do refunds work with destination charges?

By default, refunding a destination charge takes the money from the platform's balance, and the connected account keeps its transfer. To take it back from the connected account too, set `reverse_transfer`. To return the platform's fee as well, set `refund_application_fee`:

```js
await stripe.refunds.create({
  payment_intent: "pi_123",
  reverse_transfer: true,
  refund_application_fee: true,
});
```

Decide your refund policy up front: who pays for refunds, and whether the platform keeps its fee.

## 216: What are Connect embedded components?

They are ready-made UI parts you embed in your platform for connected accounts: onboarding, payments list, payouts, disputes, account management and more. You create an Account Session on the server and use Stripe's Connect.js on the front end.

```js
const accountSession = await stripe.accountSessions.create({
  account: "acct_123",
  components: { payments: { enabled: true }, payouts: { enabled: true } },
});
res.json({ clientSecret: accountSession.client_secret });
```

Sellers can manage their Stripe account without leaving your platform, and you don't have to build these screens yourself.

## 217: What are the connected account types, and what is Accounts v2?

The classic v1 account types are:

- Standard: the user has a full Stripe Dashboard and a direct relationship with Stripe.
- Express: a lighter Stripe-hosted dashboard, the platform controls more.
- Custom: no Stripe dashboard, the platform builds everything and is responsible for more.

Newer integrations describe accounts by their properties instead (who collects requirements, who pays fees, who is liable for losses, which dashboard they get). Accounts v2 (`/v2/core/accounts`) goes further and uses one account object with configurations, for example as a merchant and as a customer. Stripe's docs call the v1 Express and Custom types legacy for new work.

## 218: How do you respond to a dispute through the API?

Update the dispute with evidence and submit it:

```js
await stripe.disputes.update("dp_123", {
  evidence: {
    customer_email_address: "ana@example.com",
    product_description: "Annual Pro plan for project management software",
    service_date: "2026-10-01",
    access_activity_log:
      "User logged in 47 times between Oct 1 and Oct 28 from IP 203.0.113.5",
    uncategorized_text: "Customer used the service daily after purchase.",
  },
  submit: true,
});
```

You can also upload files (receipts, screenshots, shipping proof) with the Files API and reference them. You only get one submission, so gather everything first.

## 219: Which dispute events should you handle?

- `charge.dispute.created`: a dispute was opened. Alert your team, collect evidence, maybe pause the customer's account.
- `charge.dispute.updated`: evidence or status changed.
- `charge.dispute.closed`: the dispute is decided. `status` is `won` or `lost`.
- `charge.dispute.funds_withdrawn` and `charge.dispute.funds_reinstated`: money left or came back to your balance.

Disputes have a deadline (`evidence_details.due_by`). Missing it means you lose automatically.

## 220: What are some useful Radar rules?

Examples of custom rules:

```text
Block if :risk_level: = 'highest'
Review if :risk_score: > 65
Block if :card_country: != :ip_country: and :amount_in_usd: > 500
Request 3D Secure if :risk_level: = 'elevated'
Block if :cvc_check: = 'fail'
Allow if :customer: in @trusted_customers
```

You can also use your own data with metadata, like `Review if ::account_age_days:: < 2`, when you add `account_age_days` to the PaymentIntent metadata. Test new rules against past payments in the Dashboard before turning them on.

## 221: How can you help Radar detect fraud better?

- Load Stripe.js on all pages of your site, not just checkout. It collects signals about how the user behaves.
- Create PaymentIntents with a `customer` and pass email and address details.
- Collect a billing postal code and the CVC.
- Add your own signals in metadata (account age, number of past orders) and use them in rules.
- Mark fraudulent payments when you refund them (`reason: 'fraudulent'`), so Radar learns.

## 222: How do you handle rate limit errors from Stripe?

Retry with exponential backoff and some random jitter. The SDK does this for you when `maxNetworkRetries` is set. Look at the `Stripe-Rate-Limited-Reason` header to see whether you hit a global or endpoint limit.

Then reduce how often you hit it: use webhooks instead of polling, cache objects that rarely change (prices, products), run bulk jobs slowly with a queue, and avoid many parallel updates to the same object.

## 223: What is a lock_timeout error?

Stripe locks an object while it's being changed. If several requests try to change the same object at once (for example many updates to one customer), some may wait too long and fail with a 429 `lock_timeout` error.

The fix is to avoid concurrent writes to the same object: run them in order, for example with a per-customer queue, and retry with backoff when it happens.

## 224: How should you model payment status in your own database?

Use a small state machine for orders, separate from Stripe's statuses:

```text
pending -> awaiting_payment -> paid -> fulfilled
                           \-> failed
paid -> refunded / partially_refunded
paid -> disputed -> (won -> paid) / (lost -> charged_back)
```

Change states only on clear signals (webhooks or a fresh API read), log every change with the Stripe object ID and event ID, and reject changes that don't make sense, like `failed` after `fulfilled`. Map Stripe statuses into your states in one place.

## 225: How do you match payouts to the payments in them?

List the balance transactions included in a payout:

```js
for await (const txn of stripe.balanceTransactions.list({
  payout: "po_123",
  expand: ["data.source"],
})) {
  console.log(txn.type, txn.amount, txn.fee, txn.net, txn.source?.id);
}
```

Each transaction points to its source (charge, refund, dispute, fee). From there you find the PaymentIntent and its metadata, and so your order. This is how finance teams check that the money in the bank matches the orders. Stripe also has payout reconciliation reports for this.

## 226: How do you get the Stripe fee for a payment?

Expand the charge's balance transaction:

```js
const pi = await stripe.paymentIntents.retrieve("pi_123", {
  expand: ["latest_charge.balance_transaction"],
});
const txn = pi.latest_charge.balance_transaction;
console.log(txn.amount, txn.fee, txn.net, txn.currency);
```

The balance transaction is in your settlement currency, so it may differ from the payment currency. `fee_details` breaks down the fee into parts, like the Stripe fee and tax.

## 227: How do currency conversions show up in Stripe data?

If the customer pays in EUR and your account settles in USD, the Charge shows the EUR amount, and its balance transaction shows the USD amount, the `exchange_rate` and the fee in USD.

For reports, use the balance transaction amounts for money that actually reached you, and the charge amounts for what the customer paid. Mixing these up is a common source of reconciliation errors.

## 228: What should you avoid logging in a Stripe integration?

- Secret keys and webhook secrets.
- Client secrets of PaymentIntents and SetupIntents.
- Full request bodies from the front end, which could contain personal data.
- Full Stripe objects with customer names, emails and addresses, unless your logs are allowed to hold personal data.

Log IDs instead: `pi_...`, `cus_...`, `evt_...`, the request ID and your order ID. They are enough to find everything else.

## 229: How would you use restricted keys in a system with several services?

Give each service a key with only the permissions it needs:

- The checkout service: write access to PaymentIntents and Customers.
- The reporting job: read access to balance transactions and payouts.
- The support tool: read customers and charges, write refunds.

Name keys after the service, store them in each service's secrets, and rotate them on a schedule. If one service is compromised, the attacker can't use its key for everything.

## 230: How do you secure a webhook endpoint?

- Always verify the signature with the endpoint's secret.
- Use HTTPS (Stripe requires it in live mode).
- Don't put the endpoint behind login or CSRF checks that would block Stripe, but don't trust anything before the signature check.
- Keep the default timestamp tolerance (5 minutes) so old events can't be replayed.
- Only accept the event types you handle, and ignore the rest.
- Rate limit or size limit the endpoint like any public endpoint.

## 231: How do you rotate a webhook signing secret without missing events?

Roll the secret in the Dashboard and choose an expiry for the old one (Stripe allows the old secret to keep working for up to 7 days). During that time, Stripe signs events with both secrets.

Deploy the new secret to your servers, and check that events are verified. Some teams try both secrets in their code during the switch. After the old secret expires, remove it.

## 232: How do you create and send a one-off invoice?

```js
const invoice = await stripe.invoices.create({
  customer: "cus_123",
  collection_method: "send_invoice",
  days_until_due: 30,
});

await stripe.invoiceItems.create({
  customer: "cus_123",
  invoice: invoice.id,
  amount: 250000,
  currency: "usd",
  description: "Consulting, October 2026",
});

await stripe.invoices.finalizeInvoice(invoice.id);
await stripe.invoices.sendInvoice(invoice.id);
```

The customer gets an email with a link to pay. You get `invoice.paid` when they do.

## 233: What is a credit note?

A credit note lowers the amount of a finalized invoice without voiding it. You use it to correct mistakes or give partial refunds on invoices.

```js
await stripe.creditNotes.create({
  invoice: "in_123",
  lines: [
    { type: "invoice_line_item", invoice_line_item: "il_123", quantity: 1 },
  ],
  refund_amount: 5000,
});
```

For a paid invoice, the credit can be refunded to the card, added to the customer's credit balance or recorded as paid outside Stripe. Credit notes keep a proper paper trail, which accountants need.

## 234: What is the customer credit balance?

Each customer has a balance that is applied to their next invoices. A negative balance is a credit (Stripe owes them), a positive one is a debit.

Credits come from prorations, credit notes or manual adjustments:

```js
await stripe.customers.createBalanceTransaction("cus_123", {
  amount: -1000, // $10 credit
  currency: "usd",
  description: "Apology credit for outage",
});
```

The credit is used up on future invoices. It's not refunded to the card automatically.

## 235: How do you verify a US bank account for ACH payments?

The usual way is Financial Connections: the customer logs in to their bank inside Stripe's flow, and the account is verified right away. If that's not possible, Stripe falls back to microdeposits: small amounts are sent to the account, and the customer confirms them a day or two later.

With the Payment Element or Checkout, both flows are built in. With microdeposits, the PaymentIntent waits in `requires_action` until the customer verifies.

## 236: What should you know about SEPA Direct Debit?

- The customer gives their IBAN and accepts a mandate, which Checkout and the Payment Element show.
- Payments take several business days to succeed, and you see `processing` until then.
- The customer can ask their bank to reverse a debit for weeks after it succeeds, and longer if there was no valid mandate.
- Reversals show up as disputes, but you usually can't challenge them with evidence.

It's popular in Europe for subscriptions because it's cheap and doesn't expire like cards.

## 237: How do you set a dynamic statement descriptor?

Set a suffix per payment, which Stripe adds to your account's prefix:

```js
await stripe.paymentIntents.create({
  amount: 2500,
  currency: "usd",
  statement_descriptor_suffix: "ORDER 4821",
});
```

The full descriptor has a length limit (22 characters), so keep the suffix short. A clear descriptor reduces "unrecognized charge" disputes.

## 238: How do you show Checkout and Elements in the customer's language?

Both detect the browser language by default. You can set it yourself:

```js
// Checkout
await stripe.checkout.sessions.create({ ..., locale: 'de' });

// Elements
const elements = stripe.elements({ clientSecret, locale: 'de' });
```

Error messages from `confirmPayment()` are translated too. Receipts and invoice emails use the customer's `preferred_locales`.

## 239: What does the back end return for a mobile payment sheet?

The app needs the PaymentIntent (or SetupIntent) client secret, the Stripe customer ID if you want saved payment methods, and a short-lived credential that lets the app access that customer's saved payment methods. The publishable key can be returned too.

The server creates all of these per checkout, for the logged-in user only. The secret key never goes to the app.

## 240: How do you stop a customer from paying twice by double-clicking?

- Disable the pay button as soon as it's clicked and show a spinner.
- Reuse the same PaymentIntent for the order. A PaymentIntent can only succeed once.
- Use idempotency keys based on the order ID on the server.
- Check the order status before creating a new PaymentIntent.

The second and third points matter most, because front-end checks can be skipped.

## 241: Should you create a new PaymentIntent every time the checkout page loads?

No. Create one per order or cart, store its ID, and reuse it when the customer comes back to the page. Creating a new one each time leaves many incomplete PaymentIntents and makes it possible to pay twice for one order (once with each intent).

If the cart changes, update the existing PaymentIntent's amount. Or use the deferred intent flow, where the PaymentIntent is created only when the customer clicks "Pay".

## 242: How do you update the amount when the cart changes?

Update the PaymentIntent before it's confirmed:

```js
await stripe.paymentIntents.update(order.paymentIntentId, {
  amount: newTotalCents,
});
```

On the front end, call `elements.fetchUpdates()` so the Payment Element knows about the change (for example, to show or hide methods that depend on the amount). You can't change the amount after the payment succeeded.

## 243: What should you do with PaymentIntents that are never paid?

They don't cost anything, but they clutter your data. You can cancel them when the related order is abandoned or expires, which also releases any authorization holds:

```js
await stripe.paymentIntents.cancel(pi.id, { cancellation_reason: "abandoned" });
```

A nightly job that cancels PaymentIntents older than a few days for abandoned orders keeps things clean. Don't cancel ones that are `processing`.

## 244: How do you handle a $0 checkout?

Stripe can't charge $0. Options:

- If you want to save a card (for example a free trial), use a SetupIntent or Checkout in `setup` mode.
- For a subscription with a trial, Stripe creates a $0 invoice and handles it for you.
- For a 100% discount code on a one-time order, Checkout can complete without payment. In your own flow, skip Stripe and mark the order as paid.

Don't create a PaymentIntent with `amount: 0`, it's rejected.

## 245: Who should calculate totals with tax and discounts: you or Stripe?

Pick one source of truth. If Stripe calculates tax and discounts (Checkout, Billing, Stripe Tax), save the final totals from Stripe's objects (`amount_total`, `total_details`) in your order, instead of calculating them again yourself.

If you calculate them, send Stripe only the final amount. Calculating in both places leads to off-by-one-cent differences due to rounding, and your invoices won't match what was charged.

## 246: How do you calculate the platform's application fee?

Work in integers and round in a fixed, documented way:

```js
function applicationFee(amountCents, percent = 10, fixedCents = 30) {
  return Math.round((amountCents * percent) / 100) + fixedCents;
}
```

Decide whether your fee covers Stripe's fee (with destination charges, the platform pays Stripe fees out of its share), whether it's refunded on refunds, and how it works in other currencies. Store the fee you charged on your order for later reporting.

## 247: What is latest_charge on a PaymentIntent?

`latest_charge` is the ID of the most recent Charge created by the PaymentIntent. A PaymentIntent can create several charges if the first attempts fail, but only one can succeed.

Expand it to get the receipt URL, the card details used, the Radar outcome or the balance transaction. Older API versions had a `charges` list on the PaymentIntent instead.

## 248: How do you update your orders when a refund happens?

Listen for `charge.refunded` and `refund.updated`, find the order through the PaymentIntent's metadata, and store the refunded amount:

```js
if (event.type === "charge.refunded") {
  const charge = event.data.object;
  const pi = await stripe.paymentIntents.retrieve(charge.payment_intent);
  await orders.setRefunded(pi.metadata.orderId, {
    refundedCents: charge.amount_refunded,
    full: charge.refunded,
  });
}
```

Refunds can also be made in the Dashboard by support staff, so don't rely only on your own API calls to update orders.

## 249: What should your app do when a dispute is opened?

It depends on the business, but common steps:

- Mark the order as disputed and alert the team.
- For digital goods, consider pausing the user's access or account, since the money is gone.
- Automatically collect evidence (login logs, delivery proof) and prepare a response.
- If the customer is clearly right, accept the dispute rather than fight it.

Track your dispute rate. Card networks have programs for merchants with high rates, which lead to fines and can end your ability to accept cards.

## 250: What are early fraud warnings?

An early fraud warning (`radar.early_fraud_warning.created`) is a notice from the card issuer that a payment was reported as fraud. It often comes before a dispute.

If you refund the payment quickly after the warning, you can often avoid the dispute and its fee. Many businesses refund automatically for low-value orders when they get this event.

## 251: What would you monitor in a Stripe integration?

- Webhook delivery failures and how long events wait in your queue.
- Payment success rate and decline rate, split by payment method and country.
- Error rates and latency of your calls to Stripe.
- Rate limit (429) errors.
- Orders stuck in `awaiting_payment` or `paid but not fulfilled` for too long.
- Disputes and early fraud warnings.

Set alerts on sudden changes. A drop in success rate after a deploy is often the first sign of a bug.

## 252: How do you debug a failing API call?

1. Take the request ID from the error (`err.requestId`) or your logs.
2. Find it in the Dashboard logs. You'll see the exact request body, the response and the API version used.
3. Read `err.code`, `err.param` and `err.message`. They usually say which parameter is wrong.
4. Check if it works in a sandbox with the same parameters.

Most errors are wrong parameters, wrong key (live vs test), the wrong account in Connect, or a field that changed in a newer API version.

## 253: How should you separate environments in a Stripe integration?

- Use different sandboxes (or test mode) for local, CI and staging, and live keys only in production.
- Give each environment its own webhook endpoint and signing secret.
- Don't share Stripe IDs between environments. Use lookup keys or config per environment for prices.
- Make the app fail at startup if a live key is used outside production.

```js
if (
  process.env.NODE_ENV !== "production" &&
  process.env.STRIPE_SECRET_KEY.startsWith("sk_live_")
) {
  throw new Error("Live Stripe key outside production");
}
```

## 254: How do you set up the same products and prices in every environment?

Write a script that creates products and prices from a config file, using lookup keys so it can run again safely:

```js
for (const plan of plans) {
  const existing = await stripe.prices.list({ lookup_keys: [plan.lookupKey] });
  if (existing.data.length) continue;

  const product = await stripe.products.create({ name: plan.name });
  await stripe.prices.create({
    product: product.id,
    unit_amount: plan.amount,
    currency: "usd",
    recurring: { interval: plan.interval },
    lookup_key: plan.lookupKey,
  });
}
```

Run it for each sandbox and for live. Your code then uses lookup keys, never hardcoded `price_...` IDs. The Stripe CLI's fixtures feature is another way to do this.

## 255: How do you type webhook events in TypeScript?

`Stripe.Event` is a union of all event types. Check `event.type` and TypeScript narrows `event.data.object` to the right type:

```ts
import Stripe from "stripe";

function handle(event: Stripe.Event) {
  switch (event.type) {
    case "invoice.paid": {
      const invoice = event.data.object; // Stripe.Invoice
      return onInvoicePaid(invoice);
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object; // Stripe.Subscription
      return onSubscriptionEnded(sub);
    }
    default:
      return; // ignore other events
  }
}
```

Expandable fields are typed as `string | Stripe.Customer`, so check the type or expand before using them.

## 256: What should your handler do with event types it doesn't know?

Return 2xx and ignore them. If you return an error, Stripe keeps retrying an event you'll never handle, and the endpoint looks unhealthy.

New event types can appear after you change your subscribed events or when Stripe adds new ones. Log unknown types at a low level, so you notice if you're missing something important.

## 257: When does Stripe finalize subscription invoices?

When a subscription renews, Stripe creates the invoice as a draft and finalizes it about an hour later, then tries to collect payment. You get `invoice.created` at the start of that hour.

That hour is your chance to add extra line items (like usage you track yourself) or change the invoice. After it's finalized, the invoice can't be changed. If your webhook endpoint is failing, Stripe may wait longer before finalizing.

## 258: How do you add a one-time charge to a subscription's next invoice?

Create an invoice item for the customer and subscription. It's added to the next invoice:

```js
await stripe.invoiceItems.create({
  customer: "cus_123",
  subscription: "sub_123",
  amount: 1500,
  currency: "usd",
  description: "Extra storage, 50 GB",
});
```

To charge it right away instead, create and finalize a separate invoice. When you update a subscription, you can also pass `add_invoice_items` to add one-off items to the next invoice.

## 259: What is the billing cycle anchor?

The billing cycle anchor is the reference date that decides when renewals happen. By default it's the subscription start date, so a subscription started on the 15th renews on the 15th.

You can set it when you create the subscription, for example to bill all customers on the 1st of the month, so invoices and reports line up. The first invoice is then prorated for the time until the anchor, unless you turn proration off.

The Endive release changed how the anchor is passed, so Subscriptions and Invoices use the same format. Check the API reference for the version you're on before you copy an older example.

## 260: How do you handle frequent seat changes without confusing the customer?

If a team adds and removes users many times a month, each change can create small prorations and many invoice lines. Options:

- Add prorations to the next renewal (`create_prorations`) instead of invoicing each change.
- Only update the quantity once a day, from a job that counts active users.
- Charge for increases right away and apply decreases at the next renewal.

Stripe also limits how often a subscription's quantity can change in an hour, so batching changes helps.

## 261: Can a subscription have several prices?

Yes. A subscription can have several items, each with its own price and quantity, for example a base plan, a seat price and a metered usage price. They are billed together on one invoice.

```js
await stripe.subscriptions.create({
  customer: "cus_123",
  items: [
    { price: "price_base_monthly" },
    { price: "price_seat_monthly", quantity: 8 },
    { price: "price_api_usage" }, // metered, no quantity
  ],
});
```

All items must use the same currency, and in classic billing mode, the same interval.

## 262: How do you raise prices for existing subscribers?

Create the new Price and move subscribers to it at their next renewal. A schedule or a bulk job that updates each subscription with `proration_behavior: 'none'` does this.

Tell customers in advance (often required by law or your terms), and decide who keeps the old price ("grandfathering"). Do it in batches, and watch for payment failures and cancellations after the change.

## 263: How do you bill a company that pays by bank transfer every month?

Create the subscription with `collection_method: 'send_invoice'`:

```js
await stripe.subscriptions.create({
  customer: "cus_company",
  items: [{ price: "price_enterprise_monthly" }],
  collection_method: "send_invoice",
  days_until_due: 30,
});
```

Each period, Stripe emails an invoice with a due date. The customer pays through the hosted invoice page or by bank transfer. If they pay outside Stripe, mark the invoice paid with `paid_out_of_band: true`.

## 264: A customer's subscription is past_due. How do you let them fix it?

Let them add a new payment method (Customer Portal, or your page with a SetupIntent), set it as the default, then pay the open invoice right away instead of waiting for the next retry:

```js
await stripe.customers.update("cus_123", {
  invoice_settings: { default_payment_method: newPmId },
});

const sub = await stripe.subscriptions.retrieve("sub_123");
await stripe.invoices.pay(sub.latest_invoice, { payment_method: newPmId });
```

If the payment works, the subscription goes back to `active` and you get `invoice.paid`.

## 265: What is invoice.payment_action_required?

It's sent when a subscription invoice payment needs the customer to authenticate, usually 3D Secure on a renewal. The payment can't go through until the customer does it.

Stripe can email the customer a link to the hosted invoice page, where they can authenticate. You can also show a banner in your app with a link to finish the payment, or confirm it with Stripe.js when they log in.

## 266: How can Stripe help recover failed payments without code?

In the Billing settings you can turn on:

- Smart Retries.
- Emails for failed payments, with a link to update the payment method.
- Emails before cards expire.
- Reminders for invoices that need 3D Secure.
- What to do when all retries fail (cancel, mark unpaid, leave past due).

These are worth turning on before writing your own dunning logic. Then use webhooks only for what's specific to your app, like limiting access.

## 267: How do you model a free plan?

There are two common ways:

- Don't create anything in Stripe for free users. A user without an active subscription is on the free plan. Simple and cheap.
- Create a $0 price and a subscription, so every user has a subscription. Upgrades are just price changes, and the Customer Portal can handle them.

The first is more common. The second makes sense if free users also have metered usage or you want all plan changes to go through Stripe.

## 268: How do you let a customer switch from monthly to yearly?

Update the subscription item to the yearly price:

```js
await stripe.subscriptions.update("sub_123", {
  items: [{ id: "si_123", price: "price_pro_yearly" }],
  proration_behavior: "always_invoice",
});
```

When the interval changes, Stripe resets the billing cycle to now and charges the yearly price minus the credit for the unused monthly time. Show the amount first with a preview invoice. For yearly to monthly, it's common to switch at the end of the year instead.

## 269: How do you collect a reason when a customer cancels?

The Customer Portal can ask for a reason and save it. With the API, pass `cancellation_details`:

```js
await stripe.subscriptions.update("sub_123", {
  cancel_at_period_end: true,
  cancellation_details: {
    feedback: "too_expensive",
    comment: "We only use it a few times a month",
  },
});
```

`feedback` takes fixed values like `too_expensive`, `missing_features`, `switched_service` and `unused`. Track these to see why people leave.

## 270: How do you add custom fields to Checkout?

Use `custom_fields` to ask for up to a few extra pieces of information:

```js
await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [{ price: "price_123", quantity: 1 }],
  custom_fields: [
    {
      key: "company",
      label: { type: "custom", custom: "Company name" },
      type: "text",
      optional: true,
    },
  ],
  success_url: "https://example.com/success",
});
```

The answers are on the completed session in `custom_fields`. For more complex forms, collect the data on your own page before Checkout.

## 271: How do you let customers change quantity in Checkout?

Set `adjustable_quantity` on the line item:

```js
line_items: [
  {
    price: 'price_ticket',
    quantity: 1,
    adjustable_quantity: { enabled: true, minimum: 1, maximum: 10 },
  },
],
```

The final quantity is in the session's line items. Read it from there when you fulfill, not from what you passed at creation.

## 272: How do you connect Payment Link purchases to your users?

Payment Links are shared URLs, so you can't set per-user data when you create them. Instead, add URL parameters when you show the link:

```text
https://buy.stripe.com/abc123?client_reference_id=user_42&prefilled_email=ana%40example.com
```

`client_reference_id` ends up on the Checkout Session. In the `checkout.session.completed` webhook, the session also has a `payment_link` field, so you know which link was used. Metadata set on the Payment Link itself is the same for every buyer.

## 273: How do you redirect customers after paying with a Payment Link?

Set `after_completion` when you create the link:

```js
await stripe.paymentLinks.create({
  line_items: [{ price: "price_123", quantity: 1 }],
  after_completion: {
    type: "redirect",
    redirect: {
      url: "https://example.com/thanks?session_id={CHECKOUT_SESSION_ID}",
    },
  },
});
```

Without it, Stripe shows its own confirmation page. As with Checkout, fulfill from the webhook, not the redirect.

## 274: How would you migrate from the Charges API and Card Element to current APIs?

1. Replace token or source creation on the client with the Payment Element (or Checkout).
2. On the server, create PaymentIntents instead of Charges. Move fulfillment from "after the API call" to webhooks.
3. Handle `requires_action` and async payment methods, which the old flow didn't have.
4. Saved cards from the old flow (sources and card objects on customers) still work with PaymentIntents, so you don't have to ask customers to re-enter them.
5. Update reports that read Charges to use PaymentIntents, and their `latest_charge`.

Run both flows side by side behind a feature flag during the move.

## 275: Should your order point to a Checkout Session or a PaymentIntent?

Store both when you use Checkout. The session is what the customer used, and it has line items, customer details and the completion events. The PaymentIntent is the actual payment, and refunds, disputes and charges link to it.

When the session completes, read `session.payment_intent` (or `session.subscription`) and save it on the order. Then later events like `charge.refunded` can be matched to the order through the PaymentIntent.

## 276: How do you send a customer straight to a specific action in the Customer Portal?

Use `flow_data` when you create the portal session:

```js
const session = await stripe.billingPortal.sessions.create({
  customer: "cus_123",
  return_url: "https://example.com/account",
  flow_data: { type: "payment_method_update" },
});
```

Other flow types include `subscription_cancel` and `subscription_update`. This is good for "Update card" buttons and email links: the customer lands on the exact step instead of the portal's home page.

## 277: How do you calculate tax with a custom Elements checkout?

Use the Tax Calculations API before you create the PaymentIntent, and record a tax transaction after the payment:

```js
const calc = await stripe.tax.calculations.create({
  currency: "usd",
  line_items: [
    { amount: 5000, reference: "sku_123", tax_behavior: "exclusive" },
  ],
  customer_details: {
    address: { country: "US", postal_code: "94103", state: "CA" },
    address_source: "shipping",
  },
});

const pi = await stripe.paymentIntents.create({
  amount: calc.amount_total,
  currency: "usd",
  metadata: { taxCalculationId: calc.id },
});

// after payment_intent.succeeded
await stripe.tax.transactions.createFromCalculation({
  calculation: calc.id,
  reference: `order-${orderId}`,
});
```

The transaction step is what makes the tax show up in Stripe Tax reports.

## 278: How do you collect addresses in an Elements checkout?

Use the Address Element. It has autocomplete and formats addresses for each country:

```js
const addressElement = elements.create("address", { mode: "shipping" });
addressElement.mount("#address-element");

const { complete, value } = await addressElement.getValue();
if (complete) {
  await fetch("/api/tax-preview", {
    method: "POST",
    body: JSON.stringify(value.address),
  });
}
```

`mode: 'billing'` is for billing addresses. You need an address before you can calculate tax, so collect it before showing the final total.

## 279: When would one app use several Stripe accounts?

Some companies have separate legal entities in different countries, each with its own Stripe account (to settle locally and meet local rules). The app then picks the right account for each customer.

In code, keep a client per account (each with its own key), store which account each customer belongs to, and give each account its own webhook endpoint or route with its own secret. Stripe Organizations help manage several accounts together.

## 280: What should you watch out for when handling webhooks in serverless functions?

- Read the raw body. Some frameworks parse it by default.
- Cold starts and short timeouts: verify, store or queue, and return fast.
- Many function instances run at once, so idempotency must use a shared database, not memory.
- Keep the Stripe client outside the handler, so it is reused between calls.
- Function logs may be your only debug tool, so log event IDs and types.

## 281: How do you structure a handler that supports many event types?

Use a map from event type to a function, and keep each function small:

```js
const handlers = {
  "checkout.session.completed": onCheckoutCompleted,
  "checkout.session.async_payment_succeeded": onCheckoutCompleted,
  "invoice.paid": onInvoicePaid,
  "invoice.payment_failed": onInvoicePaymentFailed,
  "customer.subscription.updated": syncSubscriptionFromEvent,
  "customer.subscription.deleted": syncSubscriptionFromEvent,
  "charge.refunded": onChargeRefunded,
};

export async function handleEvent(event) {
  const handler = handlers[event.type];
  if (!handler) return; // ignore
  await handler(event.data.object, event);
}
```

The same keys can be used to configure the endpoint's event list, so the two stay in sync.

## 282: How do you map Stripe objects to your own data model?

Keep your models simple and focused on what your app needs:

- `users.stripe_customer_id`
- `subscriptions(id, user_id, stripe_subscription_id, status, price_lookup_key, current_period_end, cancel_at_period_end)`
- `orders(id, user_id, status, total_cents, currency, stripe_payment_intent_id, stripe_checkout_session_id)`
- `stripe_events(id, type, processed_at)`

Don't copy whole Stripe objects into columns. Store what you query on, and fetch the rest from Stripe when needed. Some teams also keep the raw JSON for debugging.

## 283: How do discounts work on subscriptions in current API versions?

Use the `discounts` array, which can hold coupons or promotion codes:

```js
await stripe.subscriptions.update("sub_123", {
  discounts: [{ coupon: "LAUNCH50" }],
});
```

Since the Basil release the old single `coupon` and `promotion_code` parameters on subscriptions are gone, and you always use `discounts`. Discounts can be set on the subscription or on single items.

## 284: How do you limit who can use a promotion code?

Promotion codes have options for this:

- `max_redemptions`: how many times the code can be used in total.
- `expires_at`: when the code stops working.
- `customer`: only one customer can use it.
- `restrictions.first_time_transaction`: only for customers who never paid before.
- `restrictions.minimum_amount` with `minimum_amount_currency`: only for orders above an amount.

Stripe checks these rules in Checkout and on subscriptions, so you don't need your own checks. Keep a separate coupon for each campaign, so you can see in reports which one brought in which customers.

## 285: How do you clean up subscriptions that never got paid?

A subscription created with `default_incomplete` stays `incomplete` until the first payment works. If the customer never pays, after about 23 hours it becomes `incomplete_expired` and Stripe sends `customer.subscription.deleted`.

Don't give access while it's `incomplete`, and delete or mark your local record when it expires. Also stop creating a new incomplete subscription every time the user opens the checkout page. Reuse the existing one.

## 286: Should your app call Stripe on every request to check if a user has paid?

No. That's slow, uses up your rate limit and breaks your app when Stripe is slow. Keep the subscription status in your database, updated by webhooks, and read it locally.

Call Stripe directly only when you need fresh data, like right after checkout before the webhook arrives, or in a "refresh my subscription" button.

## 287: What is a grace period, and how do you implement it?

A grace period is time when the customer keeps access after a failed payment, while Stripe retries. It reduces churn from temporary card problems.

Implement it in your own access check, for example: give access if the status is `active` or `trialing`, or if it's `past_due` and the failed invoice is less than 7 days old. Show a clear banner asking the customer to update their card.

## 288: How do you implement a refund on cancellation policy?

For example, "full refund within 14 days, nothing after":

```js
async function cancelWithPolicy(sub) {
  const invoice = await stripe.invoices.retrieve(sub.latest_invoice);
  const paidAt = invoice.status_transitions.paid_at;
  const within14Days = Date.now() / 1000 - paidAt < 14 * 24 * 3600;

  await stripe.subscriptions.cancel(sub.id);

  if (within14Days) {
    const { data } = await stripe.invoicePayments.list({ invoice: invoice.id });
    const pi = data[0]?.payment?.payment_intent;
    if (pi)
      await stripe.refunds.create(
        { payment_intent: pi },
        { idempotencyKey: `refund-cancel-${sub.id}` },
      );
  }
}
```

Write the policy down, keep the logic in one place, and record what you did on your side for support.

## 289: How do you let a customer retry a failed one-time payment?

Keep the same PaymentIntent. After a decline, it goes back to `requires_payment_method`, and the customer can enter another card and confirm again with the same client secret.

Show the decline message from the error, keep the form filled in, and suggest trying another card or payment method. Don't create a new PaymentIntent for each attempt.

## 290: How do you save a card with Checkout and charge it later?

Create a Checkout Session in `setup` mode:

```js
const session = await stripe.checkout.sessions.create({
  mode: "setup",
  customer: "cus_123",
  currency: "usd",
  success_url: "https://example.com/saved",
});
```

On `checkout.session.completed`, read `session.setup_intent`, fetch it to get the `payment_method`, and store it or set it as the default. Later, charge it with an off-session PaymentIntent.

## 291: What is the difference between payment_intent.payment_failed and charge.failed?

`charge.failed` is sent for each failed charge attempt. `payment_intent.payment_failed` is sent when a payment attempt on the PaymentIntent fails, and the PaymentIntent has `last_payment_error` with the details.

In PaymentIntent-based integrations, listen to the PaymentIntent events. The charge events are mostly useful for older Charges API code or for detailed reporting.

## 292: What happens when a payout fails?

A payout can fail if the bank account is closed or the details are wrong. You get `payout.failed` with a `failure_code`, the money goes back to your Stripe balance, and Stripe may turn off payouts until you update the bank account.

On Connect, failed payouts to connected accounts are common when sellers enter wrong bank details. Notify the seller and send them to update their account.

## 293: What reporting options does Stripe give you?

- The Dashboard has built-in reports for balances, payouts and revenue.
- The Reports API generates CSV reports (like balance and payout reconciliation) that you can download in a job.
- Stripe Sigma lets you query your Stripe data with SQL in the Dashboard.
- Data Pipeline can send your Stripe data to a data warehouse.

For finance work, these are usually better than paging through the API yourself.

## 294: How are disputes on bank debits different from card disputes?

For bank debits like ACH and SEPA, the customer can ask their bank to reverse a payment, and the bank usually just returns the money. There is often no way to send evidence and win, unlike card disputes.

Plan for it: for risky customers or large amounts, wait until the debit has had time to settle before giving full access, or use cards for first payments.

## 295: How do you test that a webhook handler handles failures correctly?

Use test cards and test clocks to create the failure cases:

- `4000 0000 0000 0341`: the card attaches to a customer but payments fail. Good for testing failed renewals.
- `4000 0000 0000 0259`: creates a dispute after the payment.
- `stripe trigger invoice.payment_failed` and `stripe trigger charge.dispute.created` for quick events.

Check that your database ends up in the right state after each event, and also after the same event is sent twice.

## 296: What do you check before going live?

- Live keys and webhook secrets are in the production config, and test keys aren't.
- A live webhook endpoint exists with the right events and API version.
- Payment methods, branding, statement descriptor and receipts are set up in live mode.
- Products and prices exist in live mode, with the same lookup keys.
- Apple Pay domains are registered for the production domain.
- Error handling, logging and alerts are in place.
- You did one real payment and a refund with a real card.

## 297: How do you make your Stripe data easy to find in the Dashboard?

- Put your own IDs (order, user, tenant) in `metadata` on PaymentIntents, Customers and Subscriptions. The Dashboard search can find objects by metadata.
- Set a `description` on PaymentIntents, like "Order 4821, 2 items".
- Give Customers a name and email.
- Use clear product names and price nicknames.

Support and finance people use the Dashboard every day. If they can't find a payment from an order number, they'll come to the developers every time.

## 298: What is the difference between a SetupIntent and saving a card during payment?

A SetupIntent only saves the payment method, no money moves. Use it when there's nothing to charge yet: trials, "add a card" pages, or pay-later services.

`setup_future_usage` on a PaymentIntent charges now and saves the card in the same step. Use it when the customer is buying something and you also want to charge them later. Both run authentication when needed so later off-session payments work better.

## 299: How do you handle Connect payouts in different currencies?

Connected accounts are paid out in their own country's currency by default. If a US platform charges in USD and sends money to a seller in the UK, the transfer is converted to GBP at some point, with a conversion fee.

You can reduce conversions by charging in the seller's currency (using `on_behalf_of` or direct charges) or by letting accounts add bank accounts in more currencies where supported. Decide who pays the conversion fee and explain it in your seller terms.

## 300: What are payment method configurations?

A payment method configuration is a named set of enabled payment methods. Your account has a default one, and you can create more:

```js
await stripe.checkout.sessions.create({
  mode: "subscription",
  payment_method_configuration: "pmc_subscriptions_only",
  line_items: [{ price: "price_pro_monthly", quantity: 1 }],
  success_url: "https://example.com/success",
});
```

On Connect, the platform can manage configurations for its connected accounts. It's the current way to control which methods show up in different flows.

# Advanced Questions (301-450)

## 301: How would you design the payments part of an e-commerce back end with Stripe?

A typical setup:

- An orders service owns orders and their prices. It creates PaymentIntents or Checkout Sessions with the order ID in metadata and an idempotency key.
- A webhook endpoint verifies signatures, stores events in a table or queue and returns 200 fast.
- Workers process events with idempotent handlers and update the order state machine.
- A fulfillment service listens to your own "order paid" event, not Stripe events directly.
- A reconciliation job compares orders, Stripe payments and payouts every day.

This keeps Stripe-specific code in one place, keeps the critical path short, and lets the rest of the system work with your own domain events.

## 302: What is the source of truth for payment state: Stripe or your database?

Stripe is the source of truth for money: whether a payment succeeded, was refunded or disputed. Your database is the source of truth for your business: orders, access, what was shipped.

Your database holds a copy of the payment state that can be a bit behind. Design for that: update it from webhooks, refresh it from the API when it matters (for example before a refund decision), and run a job that finds and fixes differences.

## 303: How do you make sure an order is fulfilled exactly once?

You can't make Stripe deliver events exactly once, but you can make the effect happen once:

- Use a unique constraint, like one fulfillment row per order, or a status change that only works from `paid` to `fulfilled`.
- Do the check and the update in one transaction with a row lock, or as a conditional update: `UPDATE orders SET status = 'fulfilled' WHERE id = $1 AND status = 'paid'`.
- Make side effects like emails or shipping requests idempotent too, for example with an idempotency key based on the order ID.

Then duplicate events, retries and the success page all end up calling the same safe function.

## 304: How do you avoid calling Stripe and then failing to save the result?

If you call Stripe and then your database write fails, you have a Stripe object your system doesn't know about. Options:

- Save your record first with a `pending` status, then call Stripe with an idempotency key based on that record. On retry, the same key returns the same Stripe object.
- Use an outbox: write "create payment for order 42" to an outbox table in the same transaction as the order, and have a worker call Stripe and update the order.
- Put your IDs in metadata, so a reconciliation job can find orphaned Stripe objects and link them.

## 305: A payment succeeded in Stripe, but your server crashed before saving the order. What happens?

If you fulfill from webhooks, this is fine. The `payment_intent.succeeded` or `checkout.session.completed` event is still delivered (and retried for days), and it carries your order ID in metadata. The order gets updated when the server is back.

If you only updated the order in the request that confirmed the payment, the order stays `pending` while the customer was charged. That's why webhook-based fulfillment plus a reconciliation job is the standard approach.

## 306: How do you design idempotency keys for a multi-step payment operation?

Give each step its own key, derived from one stable operation ID:

```js
const opId = order.id; // stable across retries

const customer = await stripe.customers.create(params, {
  idempotencyKey: `${opId}:customer`,
});
const pi = await stripe.paymentIntents.create(
  { ...piParams, customer: customer.id },
  { idempotencyKey: `${opId}:payment-intent` },
);
```

If the job crashes after step one, the retry replays the customer creation (getting the same customer) and continues. Don't reuse one key for different calls, and don't include values that change between retries (like timestamps) in the key or in the parameters.

## 307: How is idempotency different in the v2 API?

In v1, Stripe saves the response of the first request and replays it for any retry with the same key, even if it was an error.

In v2, a retry with the same key is meant to complete the operation. If the first try failed partway, the retry finishes the work instead of returning the old failure. Both versions reject a reused key with different parameters. When you mix v1 and v2 calls, keep in mind which semantics you get.

## 308: How do you handle the race between the success redirect and the webhook?

The customer can land on your success page before the webhook arrives, or after. Handle both:

- The success page retrieves the Checkout Session or PaymentIntent from Stripe and shows the real status.
- If it's paid, it can call the same idempotent `fulfill()` function as the webhook.
- If it's still processing, it shows "we're confirming your payment" and polls your API or listens for an update.

Users don't see "payment pending" for a paid order, and nothing is fulfilled twice.

## 309: Two webhook events for the same order are processed at the same time. How do you avoid a mess?

Serialize work per object:

- Lock the order row (`SELECT ... FOR UPDATE`) while handling the event.
- Or route events for the same order or customer to the same queue partition, so they are processed one at a time.
- Or use optimistic locking with a version column and retry on conflict.

Combined with "fetch the latest object from Stripe", the last handler always writes the correct state, no matter which event came first.

## 310: How would you process webhooks at high volume?

- The endpoint only verifies, stores the raw event (or its ID) and returns 200.
- A queue spreads events to workers, partitioned by object or customer ID to keep related events in order.
- Workers are idempotent and retry with backoff. After several failures, events go to a dead letter queue.
- Dashboards show queue depth, age of the oldest event and failure rate.

Thin events help here, because payloads are small and workers fetch only what they need. Keep an eye on API rate limits when many workers fetch objects at once.

## 311: Your webhook endpoint was down for a day. How do you recover?

Stripe keeps retrying for up to three days in live mode, so many events will arrive by themselves once you're back. To be safe, list events from the outage window and process them through your normal idempotent handler:

```js
for await (const event of stripe.events.list({
  created: { gte: outageStart, lte: outageEnd },
  types: [
    "checkout.session.completed",
    "invoice.paid",
    "customer.subscription.updated",
  ],
})) {
  await queue.push(event);
}
```

The events API returns events from the last 30 days. Since handlers skip known event IDs, running this doesn't cause duplicates.

## 312: What stops someone from replaying an old signed webhook?

The signature covers a timestamp (`t=` in the `Stripe-Signature` header) along with the body. The SDK rejects events whose timestamp is older than the tolerance, 5 minutes by default.

So a captured request can only be replayed within that window, and your idempotency check (event ID already processed) catches those replays. Don't increase the tolerance a lot, and in the current Node SDK, passing a tolerance of 0 turns the timestamp check off, which you don't want.

## 313: How does Stripe's webhook signature verification work in detail?

The `Stripe-Signature` header looks like `t=1763550000,v1=5257a8...`. To verify:

1. Take the timestamp `t` and the raw body, and build the signed payload `t + "." + body`.
2. Compute HMAC-SHA256 of it with the endpoint secret.
3. Compare the result with each `v1` value using a constant-time comparison.
4. Check that `t` is within the tolerance.

```js
import { createHmac, timingSafeEqual } from "node:crypto";

function verify(rawBody, header, secret, toleranceSec = 300) {
  const parts = Object.fromEntries(header.split(",").map((p) => p.split("=")));
  const expected = createHmac("sha256", secret)
    .update(`${parts.t}.${rawBody}`)
    .digest();
  const actual = Buffer.from(parts.v1 ?? "", "hex");
  const fresh = Math.abs(Date.now() / 1000 - Number(parts.t)) <= toleranceSec;
  return (
    fresh &&
    actual.length === expected.length &&
    timingSafeEqual(actual, expected)
  );
}
```

This is simplified (the header can have several `v1` values during secret rotation). Use the SDK in real code.

## 314: What are the trade-offs of thin events?

Pros:

- You always fetch current data, so out-of-order delivery matters less.
- Payloads don't depend on the endpoint's API version, which makes upgrades easier.
- Smaller payloads, less personal data in your logs and queues.

Cons:

- Every event costs at least one API call, which uses rate limit and adds latency.
- If an object changes again before you fetch it, you never see the state in between, so you can't rely on `previous_attributes` style diffs.

For most business logic ("sync the current state") thin events fit well.

## 315: How do you move to a new major API version when webhooks are involved?

1. Upgrade the SDK and code in a branch, and fix all type errors and field changes.
2. Create a second webhook endpoint with the new API version, pointing to a new route (or a flag on the same route).
3. Deploy code that can read both shapes. Process events from the new endpoint and skip duplicates by event ID.
4. Switch the account's default version if you use it, then disable the old endpoint.

Events created before the switch keep their old shape, so the code that handles retried old events must still work for a few days.

## 316: The Endive release removed payment_method_types from PaymentIntent and Checkout create calls. How do you migrate?

Code like `payment_method_types: ['card']` fails on Endive and newer versions. To migrate:

1. Turn on the methods you want in the Dashboard (dynamic payment methods).
2. Where a flow needs a different set, create a payment method configuration and pass `payment_method_configuration`.
3. Remove `payment_method_types` from create, update and confirm calls.
4. Test flows that used to be card-only. New methods may appear, like bank debits that need async handling.

The last step is the one people forget. Turning on more methods means more statuses and webhook events to handle.

## 317: How do you migrate from legacy usage records to Billing Meters?

The old API (`createUsageRecord`, `aggregate_usage` on prices) was removed in the Basil release. To migrate:

1. Create a Meter for each usage type with the right aggregation (sum, count or last).
2. Create new metered Prices linked to the meters.
3. Change your reporting code to send meter events with the customer ID and a unique `identifier`.
4. Move subscriptions to the new prices at a period boundary, so you don't bill the same usage twice.

Meter events are linked to customers, not subscription items, which also makes plan changes simpler.

## 318: What is the flexible billing mode for subscriptions?

Subscriptions have a `billing_mode` that is either `classic` or `flexible`. Flexible mode is the default for new subscriptions on the Clover release and later. It allows things classic mode doesn't, like items with different intervals on one subscription and more accurate prorations, and it's needed for some newer billing features.

You can move an existing subscription from classic to flexible with the migrate endpoint, but not back. If you have old subscriptions, expect a mix of both modes and test plan changes and prorations in each.

## 319: How would you design subscription access control in your app?

- Keep a local subscription table synced from Stripe.
- Write one function, `hasAccess(account)`, that decides based on status, plan and your rules (grace period for `past_due`, access until period end for `cancel_at_period_end`).
- Map prices to features in one place (or use Stripe Entitlements).
- Cache the result per request, not for long.

Never spread checks like `status === 'active'` around the codebase. When rules change, you want to change one function.

## 320: What are some tricky proration cases?

- Several plan changes in one period: each creates its own prorations, and the invoice can be hard for customers to read.
- Downgrades create credits, not refunds. The credit sits on the customer balance until the next invoice.
- Changing the billing interval resets the billing cycle.
- Trials: changes during a trial don't create prorations, since nothing was charged.
- Quantity going down then up in the same period can create a credit and a charge that almost cancel out.

Preview invoices before changes, and consider `proration_behavior: 'none'` for changes you want to apply only from the next period.

## 321: A customer downgrades and wants their money back. How do you handle it?

A downgrade with prorations leaves a credit on the customer's balance, which pays future invoices. If they want cash back:

1. Calculate the credit (from the proration invoice lines or the customer balance).
2. Refund that amount on the last paid invoice's payment.
3. Remove the credit from the customer balance with a balance transaction, so it's not used twice.

Or use a credit note on the paid invoice with a refund amount, which does both in one step and keeps the documents right. Decide on a policy so support doesn't invent one each time.

## 322: How do you build a reliable usage reporting pipeline for meters?

- Record usage in your own database first, with a unique ID per event.
- Send meter events from a worker, using that ID as the meter event `identifier`, so retries don't double count.
- Aggregate in your system when possible (for example per minute), so you send fewer events.
- Watch for meter error events (`billing.meter.error_report_triggered`) for bad events, like an unknown customer.
- Send late events before the invoice is finalized, or bill them in the next period.

Stripe limits meter events per customer and meter at the same time, and has a separate high-throughput meter event stream in the v2 API for large volumes.

## 323: How do invoices with partial payments affect your code?

Since Basil, one invoice can be paid by several payments, for example two cards, or a partial payment now and the rest later. The invoice tracks `amount_paid` and `amount_remaining`, and the payments are listed separately.

Code that assumes "one invoice, one PaymentIntent" needs to change: look up payments through the invoice payments list, mark orders paid when the invoice is `paid`, not when one payment succeeds, and handle refunds per payment.

## 324: You're building a marketplace where buyers order from several sellers in one cart. Which charge type would you use?

Separate charges and transfers. You charge the buyer once on the platform, then create one transfer per seller with the same `transfer_group`. Destination charges only support one destination per payment, and direct charges would need one payment per seller.

The platform pays Stripe fees and is responsible for refunds and disputes, so price your fee to cover that and keep enough balance for refunds. Tie transfers to the charge with `source_transaction` so they don't fail while funds are pending.

## 325: What does merchant of record mean, and why does it matter for platforms?

The merchant of record is the business that legally sells to the customer. Its name is on the statement, it's responsible for refunds and disputes, and its country decides the rules and fees.

On Connect, direct charges and `on_behalf_of` make the connected account the merchant. Destination charges without `on_behalf_of` make the platform the merchant. This choice affects taxes, liability, statement descriptors and which country's rules apply, so involve legal and finance when choosing.

## 326: What happens when a connected account's balance goes negative?

Refunds and disputes can take more money than the account has, for example when the seller already got paid out. Depending on who is liable for losses, Stripe may take the missing amount from the platform's balance, debit the seller's bank account, or hold future payouts until the balance is positive.

Platforms reduce this risk with payout delays, reserves (keeping part of the funds for a while), limits for new sellers, and reversing transfers when they refund.

## 327: How do you recover dispute losses on destination charges?

With destination charges the platform's balance pays for the dispute, even though the seller got the money. To recover it, reverse the transfer:

```js
await stripe.transfers.createReversal("tr_123", {
  amount: 5000,
  metadata: { disputeId: "dp_123" },
});
```

This only works if the seller's balance has the money. Your seller terms should say who pays for disputes, and your system should do the reversal when the dispute is created or lost, depending on your policy.

## 328: How do you handle changing verification requirements for connected accounts?

Stripe can ask for more information over time, for example when a seller's volume grows or rules change. Watch these fields on `account.updated`:

- `requirements.currently_due` and `requirements.current_deadline`: needed now, or charges or payouts will be paused.
- `future_requirements`: needed later, after a known date.
- `requirements.disabled_reason`: why the account can't charge or get paid.

Show sellers a clear message and a link to onboarding (Account Link or embedded component) when anything is due. Don't wait until payouts are paused.

## 329: What is a card testing attack, and how do you defend against it?

Fraudsters use your checkout to test stolen card numbers with small payments. You see many small, failed payments, often from bots, and your account's decline rate goes up.

Defenses:

- Rate limit payment attempts per IP, session and account.
- Add CAPTCHA or bot detection on the payment form.
- Require login or email verification before checkout.
- Don't create PaymentIntents for anonymous visitors in bulk (deferred intent creation helps).
- Use Radar rules that block on many declines from one IP or card fingerprint.

Stripe also detects card testing and blocks some of it, but your own limits matter.

## 330: When should you ask for 3D Secure when it isn't required?

3DS adds friction and lowers conversion, but it shifts fraud liability to the issuer in many cases. Requesting it on risky payments is a good middle ground:

```text
Request 3D Secure if :risk_level: = 'elevated'
Request 3D Secure if :amount_in_usd: > 1000
```

Ask for it on high-value orders, digital goods that can be resold, and first purchases from new accounts. Don't force it on every payment unless fraud is a big problem, because some customers will drop off.

## 331: How do you prepare for "friendly fraud" disputes?

Friendly fraud is when a real customer disputes a payment they made, for example saying they don't recognize it or never got the product. To win these:

- Keep logs: logins, IP addresses, device info, downloads, usage of the service.
- Keep delivery proof with tracking.
- Show clear terms and cancellation policies at checkout, and record that the customer accepted them.
- Use a clear statement descriptor.

Automate evidence collection, so when `charge.dispute.created` arrives, a draft response is ready. Stripe's Smart Disputes can also build and submit evidence for some disputes.

## 332: How can you improve your payment authorization rate?

- Use clear statement descriptors and accurate business details.
- Collect full billing details and the CVC.
- Save cards with SetupIntents or `setup_future_usage`, so later payments are marked correctly as merchant-initiated.
- Let Stripe use network tokens and card account updater, which keep saved cards current.
- Retry soft declines at better times (Smart Retries for subscriptions).
- Offer local payment methods where cards decline more often.

Measure the authorization rate by country, card type and flow, so you can see where declines come from.

## 333: Which failed payments should you retry, and which not?

Soft declines can work on a retry: insufficient funds, issuer unavailable, processing errors. Hard declines won't work and shouldn't be retried: stolen or lost card, closed account, invalid number, `do_not_honor` repeated many times.

Card networks limit how many times you can retry a declined card, and too many retries can bring fines. For subscriptions, let Smart Retries decide. For your own retries, use the decline code, wait between attempts and stop after a few tries.

## 334: What are SCA exemptions and merchant-initiated transactions?

Not every European payment needs SCA. Common exemptions:

- Low-value payments under a set amount.
- Transaction risk analysis: low-risk payments under certain amounts, decided by the issuer or acquirer.
- Merchant-initiated transactions (MIT): you charge a saved card without the customer, under an agreement they made earlier.

Stripe requests exemptions for you when possible. Your job is to save cards properly (SetupIntent or `setup_future_usage: 'off_session'`) and pass `off_session: true` on later charges, so payments are marked as MIT. The issuer can still ask for authentication anyway.

## 335: How do Checkout and Elements differ for PCI compliance?

With Checkout (hosted), the payment page is Stripe's, so your site isn't involved in collecting card data. This usually fits SAQ A, the simplest form.

With Elements, card fields are Stripe iframes, but they live on your page. Your page's scripts could, in theory, be changed to show a fake form. Elements integrations can still qualify for SAQ A, but you must protect the page: control which scripts load, use CSP, and keep third-party scripts off payment pages. Check the current PCI guidance with your compliance team.

## 336: How do you set up a Content Security Policy for Stripe.js?

Allow Stripe's script, frame and connect origins. A typical policy includes:

```text
script-src 'self' https://js.stripe.com;
frame-src https://js.stripe.com https://hooks.stripe.com;
connect-src 'self' https://api.stripe.com;
img-src 'self' https://*.stripe.com;
```

Payment methods, 3D Secure and wallets can need more domains, so check Stripe's CSP docs for the products you use. Test in report-only mode first. A strict CSP is one of the best protections against scripts that steal payment data.

## 337: What are common authorization bugs in payment endpoints?

- Creating a portal session for a customer ID taken from the request, letting a user manage someone else's billing.
- Returning a PaymentIntent's client secret for an order that belongs to another user.
- Letting the client pass `amount`, `price` or `customer`.
- Refund endpoints that don't check the user's role or the order owner.
- Success pages that show order details for any `session_id` in the URL.

Always look up Stripe IDs from your own database based on the logged-in user, never from request parameters alone.

## 338: Can you trust metadata in webhook events?

The event is signed, so you know Stripe sent it. But metadata is whatever was set when the object was created. If any of it came from the client (for example a `userId` passed in the request body and copied into metadata), a user could have set someone else's ID.

Set metadata only from server-side data, and in the webhook, check it against your database: the order should exist, belong to the right user, and have the same amount and currency as the payment.

## 339: How do you protect your webhook endpoint from abuse?

The endpoint is public, so anyone can send requests to it. Verify the signature before doing any work, and return 400 quickly for bad ones. Limit the body size, rate limit by IP at the edge, and don't do expensive work (database queries, API calls) before verification.

Some teams also allow only Stripe's published webhook IP addresses at the firewall. That adds defense, but the signature check is the real protection.

## 340: Why would you build a ledger next to Stripe, and how would it look?

When money moves between several parties (customers, sellers, the platform, refunds, fees), you need an exact record of who owes what. Stripe has its own balances, but they don't know your business rules.

A double-entry ledger records each movement as entries that add up to zero:

```text
Payment of $100 with a $3.20 Stripe fee and a $10 platform fee:
  debit  stripe_balance        96.80
  debit  stripe_fees            3.20
  credit seller_payable        90.00
  credit platform_revenue      10.00
```

Entries are append-only. Refunds and disputes add new entries instead of editing old ones. Each entry links to the Stripe object ID, so you can reconcile with Stripe's balance transactions.

## 341: How would you build a daily reconciliation job?

1. Pull all balance transactions for the day (or each payout) from Stripe.
2. Match each one to your records: charges to orders, refunds to refund records, disputes to disputed orders, transfers to seller payouts.
3. Flag mismatches: Stripe payments with no order, paid orders with no payment, amount differences, missing refunds.
4. Check that the payout total matches the deposit in your bank account.
5. Report differences to a dashboard or channel for someone to fix.

Run it every day. Small mismatches are easy to fix when they're one day old and very hard after six months.

## 342: How do you record refunds, disputes and fees in your books?

- Refunds: a new negative entry linked to the original payment. Stripe usually doesn't return its processing fee on refunds, so the fee stays as a cost.
- Disputes: when opened, the amount and the dispute fee leave your balance. If you win, the amount comes back as a new entry, not by deleting the first one.
- Fees: record them from the balance transactions (`fee` and `fee_details`), not from a rate in your code.
- Currency conversion: record the amounts in your settlement currency from the balance transaction.

Every entry should point to the Stripe object, so you can always explain a number.

## 343: How do you stay within Stripe rate limits at scale?

- Don't poll. Use webhooks to learn about changes.
- Cache read-mostly data like products, prices and customer details, and refresh it from webhooks.
- Run backfills and batch jobs through a rate-limited queue.
- Avoid fetching the same object many times in one request path.
- Spread scheduled jobs so they don't all start at midnight.

Stripe also limits how many reads you can make in total relative to your payment volume. Integrations that read far more than they write (for example polling every customer's subscription) can hit this, so build around your own database copy.

## 344: How do you cache Stripe data safely?

Cache what changes rarely and has clear change events:

- Products and prices: refresh on `product.*` and `price.*` events, and on deploy.
- Subscription status: store in your database from `customer.subscription.*` events.
- Customer details: update on `customer.updated`.

Don't cache payment state for decisions that move money, like "can I refund this?". Fetch fresh data for those. Add a time-based expiry as a backup in case an event is missed.

## 345: Many workers update the same Stripe customer at once and get lock_timeout errors. What do you do?

Stripe serializes writes to the same object. When many requests hit one customer, they queue and time out. Fixes:

- Process work for each customer in order, for example with a queue keyed by customer ID.
- Combine changes into one update instead of many small ones.
- Avoid writes you don't need, like updating metadata on every login.
- Retry with backoff and jitter when a lock timeout happens.

The same applies to subscriptions with many quick quantity changes.

## 346: How would you run a backfill over all your customers without hitting rate limits?

Use auto-pagination for reads and a concurrency limit for writes:

```js
import pLimit from "p-limit";

const limit = pLimit(5); // at most 5 calls at the same time
const tasks = [];

for await (const customer of stripe.customers.list({ limit: 100 })) {
  if (customer.metadata.tenantId) continue;
  tasks.push(
    limit(() =>
      stripe.customers.update(
        customer.id,
        { metadata: { tenantId: lookupTenant(customer.email) } },
        { idempotencyKey: `backfill-tenant-${customer.id}` },
      ),
    ),
  );
}
await Promise.all(tasks);
```

Make it resumable (skip already done items), log progress, and run it in quiet hours. For millions of items, process in chunks instead of keeping all tasks in memory.

## 347: How do you migrate customers and saved cards from another payment provider to Stripe?

You can't export card numbers yourself. Card data has to move between the providers directly through a secure PCI-compliant data migration. Stripe has a process for importing card data from other processors, and the old provider must agree to export it.

Plan it: map old customer IDs to new Stripe customers (keep the old ID in metadata), migrate subscriptions with the same billing dates, run a test import first, and keep the old provider running until all customers are moved. Expect some cards to fail and plan a "please update your card" flow for them.

## 348: When does it make sense to use more than one payment processor?

Reasons: better rates in some countries, local payment methods another provider handles better, or a backup if one provider is down. Large companies sometimes route payments across providers to improve authorization rates.

The costs are big: two integrations, two sets of webhooks, saved cards that don't move between providers easily, and harder reconciliation. For most companies one provider is the right choice until volume makes the savings worth it.

## 349: How should your app behave if Stripe has an outage?

- Show a clear "payments are temporarily unavailable" message instead of failing in random ways.
- Use timeouts, so slow Stripe calls don't block your servers.
- Let users keep using parts of the app that don't need Stripe, by reading subscription status from your own database.
- Queue non-urgent work (like syncing data) and retry later.
- Don't mark orders as failed because a call timed out. The outcome is unknown, so check it later.

Watch Stripe's status page and set alerts on your own Stripe error rates.

## 350: A call to create a payment timed out. Did the customer get charged?

You don't know. The request may have reached Stripe and succeeded, or not. Don't assume it failed and create a new payment, or you might charge twice.

Retry with the same idempotency key. If the first request worked, Stripe returns the same result. If it never arrived, it runs now. If you have no key, look up the PaymentIntent by its ID or by your order ID in metadata before doing anything else.

## 351: The customer paid but closed the browser during the 3D Secure redirect. How does your app find out?

The customer may never reach your `return_url`. The PaymentIntent still finishes in Stripe (or stays in `requires_action` if they didn't complete 3DS), and you get `payment_intent.succeeded` or nothing.

So the webhook drives the order state. For PaymentIntents left in `requires_action`, a job can email the customer a link back to the checkout after some time, and cancel the PaymentIntent if they don't come back.

## 352: How would you organize tests for a payment integration?

- Unit tests: your pricing, fee calculation, state machine and access rules, with Stripe mocked behind your own module.
- Handler tests: webhook handlers fed with saved event JSON and signed test headers, checking database state and duplicate handling.
- Integration tests: a sandbox with test cards for the main flows (success, decline, 3DS, refund).
- Billing tests: test clocks for renewals, failed payments, trial ends.
- Manual checks before releases: one real card payment and refund in live mode.

Most bugs are in your state handling, not in the Stripe calls, so put most effort in the first two.

## 353: How would you use test clocks in CI?

Create a fresh test clock per test run, so tests don't share state. Run the flow, advance the clock, then wait until the clock's status is `ready` before checking results:

```js
async function advanceAndWait(clockId, toTime) {
  await stripe.testHelpers.testClocks.advance(clockId, { frozen_time: toTime });
  for (let i = 0; i < 30; i++) {
    const clock = await stripe.testHelpers.testClocks.retrieve(clockId);
    if (clock.status === "ready") return;
    await new Promise((r) => setTimeout(r, 2000));
  }
  throw new Error("test clock did not finish advancing");
}
```

Delete the clock at the end, which also deletes its customers. Events from the clock go to your webhook endpoint, so CI needs a reachable endpoint (or `stripe listen`).

## 354: How do you protect yourself from breaking changes in Stripe responses?

- Pin the API version (the SDK does this) and upgrade on purpose.
- Use the TypeScript types, so field changes show up as compile errors when you upgrade.
- Save real event payloads from a sandbox as test fixtures, and refresh them when you upgrade.
- Read only the fields you need, and fail loudly when an expected field is missing instead of treating it as `undefined`.

This way an upgrade breaks in CI, not in production.

## 355: How do you trace a payment through your system?

Use correlation IDs. Put your order ID in Stripe metadata, log it with every Stripe request ID, and include it in the queue messages and logs of your webhook workers.

In distributed tracing (like OpenTelemetry), add the Stripe object IDs as span attributes. Then you can follow one payment from "create PaymentIntent" through "webhook received" to "order fulfilled", and see where time is spent or where it stopped.

## 356: What alerts would you set up for a payment system?

- Webhook queue age above a few minutes.
- Webhook handler failure rate or growing dead letter queue.
- Payment success rate dropping compared to the same hour last week.
- Spikes in declines with a single code, or in Radar blocks (possible card testing).
- Reconciliation finding mismatches.
- Orders paid but not fulfilled after a set time.
- New disputes and early fraud warnings.

Make each alert say what to check first, so the on-call person knows what to do at 3 AM.

## 357: How do you handle a GDPR deletion request for a customer with Stripe data?

- Delete or anonymize the user in your system.
- Delete the Stripe Customer (`stripe.customers.del()`), which removes saved payment methods and stops subscriptions. Cancel subscriptions first on purpose, so it's not a side effect.
- Payment records (charges, invoices) may need to be kept for tax and legal reasons. Stripe keeps them under its own legal duties, and your accountants may need your copies too.
- Remove personal data you put in metadata or descriptions.

Write down what you delete and what you keep and why, so you can answer the customer clearly.

## 358: A marketplace needs to refund a buyer after the seller was already paid out. What happens?

With destination charges, the refund comes from the platform's balance. You can reverse the transfer to take the money back from the seller, but their balance may be empty because they were paid out. Then the seller's balance goes negative, and depending on your setup, Stripe recovers it from future payments, debits their bank account, or the platform covers it.

To reduce this, delay seller payouts until the return window is over, keep a reserve for new sellers, and make sellers agree to refund terms.

## 359: How can a platform hold funds before paying sellers?

- Use separate charges and transfers, and only create the transfer when the order is delivered or the return window ends.
- Set connected accounts to manual payouts or a delayed payout schedule, and trigger payouts yourself.
- Use authorize-then-capture for short holds (days, not weeks).

There are limits: holding money for too long can turn into a regulated activity, and Stripe limits how long funds can stay unpaid in some regions. Check with Stripe and a lawyer before building an escrow-like product.

## 360: How would you handle payments for a service where the final amount isn't known at booking time?

For example a hotel, car rental or a ride:

- At booking, authorize an estimate with `capture_method: 'manual'`.
- If the cost goes up and the card supports it, use incremental authorization. Otherwise, capture the authorized part and charge the rest separately off-session.
- At the end, capture the final amount (up to the authorized amount). The rest is released.
- If the service takes longer than the authorization window, save the card with a SetupIntent at booking and charge off-session at the end instead.

Tell customers clearly about holds, because they see the held amount on their card.

## 361: How do you use a customer's saved card on a connected account?

Cards saved on the platform can't be used directly for direct charges on a connected account. You clone the PaymentMethod to the connected account:

```js
const pm = await stripe.paymentMethods.create(
  { customer: "cus_platform123", payment_method: "pm_platform123" },
  { stripeAccount: "acct_seller123" },
);

await stripe.paymentIntents.create(
  {
    amount: 5000,
    currency: "usd",
    payment_method: pm.id,
    confirm: true,
    off_session: true,
  },
  { stripeAccount: "acct_seller123" },
);
```

This lets customers save a card once on your platform and pay many businesses with direct charges.

## 362: Where should customers live in a Connect platform: on the platform or on connected accounts?

With destination charges and separate charges and transfers, customers live on the platform. One customer can buy from many sellers, and saved cards work everywhere.

With direct charges, the payment is on the connected account, so the customer must exist there too (created directly or cloned from the platform). Many SaaS platforms keep a platform customer for the customer's identity and create per-account customers only when needed.

## 363: How do you handle a platform where sellers are in many countries?

- Use `on_behalf_of` or direct charges so payments settle in the seller's country and currency, and the seller's name shows on statements.
- Check which charge types and features are supported between your platform's country and each seller's country, since cross-border rules differ.
- Price in the buyer's currency, and be clear about who pays conversion fees.
- Use Stripe-hosted or embedded onboarding, which knows each country's verification requirements.

Test with connected accounts from each main country, because the rules really are different.

## 364: What are instant payouts and what should you watch out for?

Instant payouts send money to an eligible debit card or bank account within minutes, for a fee. Gig economy platforms often offer them to workers.

Watch out for: the fee (decide who pays it), the risk of paying out money that might later be refunded or disputed, daily limits, and eligibility, since not every bank or card supports it. Many platforms only offer instant payouts to sellers with a good history.

## 365: How does manual review in Radar work in your system?

A Radar rule can send payments to review. The payment still succeeds, but it shows in the review queue. You get `review.opened`, and later `review.closed` with the result (approved, refunded, refunded as fraud).

In your system, hold fulfillment while a review is open, for example with an `in_review` order state. When the review closes as approved, fulfill. When it's refunded, cancel the order. Otherwise you'll ship goods for payments your team is about to refund.

## 366: How do you design fulfillment for payment methods that can take days to settle?

- Model a `payment_processing` order state between `awaiting_payment` and `paid`.
- Tell the customer clearly that payment is pending, by email and on the order page.
- For digital goods, decide whether to give access during processing (good UX, some risk) or wait.
- For physical goods, wait for success before shipping.
- Handle the late failure path: cancel the order, release stock and notify the customer.

Checkout reports these via `checkout.session.async_payment_succeeded` and `async_payment_failed`. With PaymentIntents, use `payment_intent.succeeded` and `payment_intent.payment_failed`.

## 367: An ACH payment succeeded, but weeks later the money was taken back. How do you design for this?

ACH debits can be returned or disputed after they show as succeeded, for example if the customer says they didn't authorize it. You'll see it as a dispute or a failed charge on a payment you already treated as paid.

Design for it: keep the order linked to the payment so you can act later, revoke access or flag the account when a return comes in, and for high-value first orders, wait some days before releasing goods. Watch your return rate, because banks and Stripe have limits for it.

## 368: How would you design checkout for customers in many countries?

- Use Checkout or the Payment Element with dynamic payment methods, so each customer sees the methods common in their country.
- Show prices in local currency, either with prices per currency or Adaptive Pricing.
- Calculate tax by location with Stripe Tax.
- Localize the page language and address formats.
- Handle async methods, since many local methods confirm later.
- Check legal requirements per country (consumer rights, invoices, tax registration).

Roll out country by country and watch conversion and authorization rates in each.

## 369: What tax edge cases should a back-end developer know about?

- B2B reverse charge: in the EU, a business customer with a valid VAT ID often pays no VAT, and the invoice must say so.
- Tax-inclusive vs tax-exclusive prices: in Europe consumer prices usually include VAT, in the US tax is added. Set `tax_behavior` on prices accordingly.
- Tax-exempt customers, like some non-profits, need `tax_exempt` set on the Customer.
- Digital goods are taxed where the customer is, which needs location evidence.
- Rates change, and old invoices must keep the old rate.

Stripe Tax handles calculation, but someone still needs to set registrations, product tax codes and prices correctly.

## 370: Why can't you edit a finalized invoice, and how do you fix mistakes?

A finalized invoice is a legal document with a number. Editing it would break audit trails and tax rules. Stripe only allows changes while the invoice is a draft.

To fix a mistake: void the invoice if it isn't paid and issue a new one, or issue a credit note (with a refund or a credit) if it was paid. For subscription invoices, catch problems during the draft hour, for example with a check in your `invoice.created` handler.

## 371: How do you migrate existing subscriptions from another billing system to Stripe?

- Create customers and import payment methods first (through a card data migration if needed).
- Create subscriptions that keep each customer's current billing date: use a trial until the next renewal date, so nobody is charged twice in the same period, or set the billing cycle anchor.
- Use `backdate_start_date` if you want the subscription's start date to match the original one.
- Turn off prorations for the import.
- Cancel subscriptions in the old system only after the Stripe ones are created and checked.

Migrate in batches, starting with a small group, and compare the first renewals in both systems.

## 372: How would you move thousands of subscribers to a new price?

1. Create the new Price and decide the effective date and who is excluded.
2. Notify customers ahead of time, as your terms and local law require.
3. Run a job that updates each subscription (or creates a schedule that changes the price at the next renewal), with `proration_behavior: 'none'`, an idempotency key per subscription, and rate limiting.
4. Record which subscriptions were moved, so the job can resume and you can report on it.
5. Watch for failed payments, cancellations and support tickets after the first renewals.

Test the job on a copy in a sandbox with test clocks first.

## 373: How do you keep seat counts in sync without too many updates?

Stripe limits how many times a subscription's quantity can change per hour and how many invoices it can get per day. A busy team adding users one by one can hit those limits.

Instead of updating on every change, mark the account as "seat count changed" and run a job (for example every hour or once a day) that sets the quantity to the current count. Charge for increases immediately only if your pricing really needs it. This also gives customers cleaner invoices.

## 374: How would you model a plan with a base fee, included usage and overage?

For example: $49 per month including 10,000 API calls, then $0.002 per call.

- A licensed recurring price for the $49 base fee.
- A metered price with graduated tiers: the first 10,000 units at $0, and the rest at $0.002.
- Both as items on one subscription.

Send usage to the meter as normal. The tiers handle the included amount, so you don't need to subtract it yourself. Show customers their current usage in your app, so overage charges aren't a surprise.

## 375: How would you implement prepaid credits?

Customers buy credits up front and use them over time. Options:

- Stripe Billing credits: credit grants that apply to usage-based charges on future invoices.
- Customer credit balance: simple, but it applies to the whole invoice, not only usage.
- Your own credit ledger: the customer buys a credit pack (a one-time payment), you track the balance in your system and stop or charge when it runs out.

Your own ledger gives the most control (expiry dates, per-feature credits) but you must build reporting and refunds yourself.

## 376: How do you handle refunds for usage-based billing?

The invoice was for real usage, so refunds are usually partial and need a reason: a bug that counted usage wrongly, an outage, a goodwill gesture.

Use credit notes on the invoice (with a refund or a credit to the customer balance), so the invoice and accounting stay correct. If a bug sent wrong meter events, fix the data for the current period before the invoice is finalized, which is cleaner than refunding later.

## 377: What is revenue recognition, and why does it matter for subscriptions?

Revenue recognition is the accounting rule for when money counts as earned. If a customer pays $1,200 for a year in January, you earn $100 each month, not $1,200 in January. The rest is "deferred revenue".

For developers, this means finance needs data about service periods, refunds, credits and plan changes, not just payment amounts. Stripe has a Revenue Recognition product that builds these reports from Billing data, which saves a lot of custom work.

## 378: When should you fetch from Stripe and when read your own copy?

Read your own copy for anything on a hot path: page loads, access checks, lists in your UI. It's fast and doesn't use rate limits.

Fetch from Stripe when you're about to move money (refund, charge, change a plan), when the user just finished something and the webhook may not have arrived, or when your copy looks wrong. After fetching, update your copy, so the next read is right too.

## 379: How do you route webhooks for several developers and environments?

- Each developer uses `stripe listen` against their own sandbox, so local events don't reach shared environments.
- Staging and production have their own endpoints and secrets, in separate sandboxes or accounts.
- If several environments share one sandbox, put an environment tag in metadata and have each environment ignore objects that aren't its own.

Separate sandboxes are much simpler than filtering, so prefer them.

## 380: How do you type expandable fields safely in TypeScript?

Expandable fields are typed as `string | Stripe.Customer | Stripe.DeletedCustomer` and similar. Write small helpers instead of casting:

```ts
function customerId(
  c: string | Stripe.Customer | Stripe.DeletedCustomer | null,
): string | null {
  if (!c) return null;
  return typeof c === "string" ? c : c.id;
}

function expanded<T extends { id: string }>(value: string | T): T {
  if (typeof value === "string")
    throw new Error(`Expected expanded object, got ID ${value}`);
  return value;
}
```

Use `expanded()` only where you passed `expand`. This avoids `undefined` errors when a field turns out to be just an ID.

## 381: What should you watch for when a webhook handler calls other services?

The handler may run more than once, so every outgoing call must be safe to repeat: use idempotency keys for other APIs, check "already sent" flags for emails, and make database updates conditional.

Also think about partial failure: if step two of three fails, a retry should continue, not start over and redo step one. Often the cleanest design is for the handler to only update your database and emit internal events, and let other services react to those events with their own retries.

## 382: What do you do with an event that always fails to process?

That's a poison event. If it keeps failing, it blocks the queue (with ordered processing) or keeps using resources. After a set number of retries, move it to a dead letter queue and alert someone.

Store the event ID, error and stack trace. After fixing the bug, replay events from the dead letter queue through the normal handler. Since handlers are idempotent, replaying is safe.

## 383: How would you make sure you never miss a webhook event?

You can't fully rely on delivery, so add a safety net:

- Return 2xx only after the event is safely stored.
- Run a periodic job that lists recent events from the API (for example the last hour) and processes any it hasn't seen.
- Run reconciliation on business data: paid invoices vs active subscriptions, succeeded payments vs paid orders.
- Alert when the endpoint shows failures in the Dashboard.

Webhooks give speed. The periodic checks give correctness.

## 384: A customer says they were charged twice. How do you investigate?

1. Find the customer in Stripe and list their recent payments. Are there two succeeded PaymentIntents, or one payment and one authorization hold that will drop off?
2. If there are two payments, check the metadata: same order ID? Different orders?
3. Look at your logs for the two creation requests: same idempotency key? Two clicks? Two tabs? A retry without a key?
4. Refund the duplicate right away and apologize.
5. Fix the root cause: reuse one PaymentIntent per order, add idempotency keys, check the order status before creating a payment.

Holds are a common false alarm: a failed or canceled authorization can show on the card for a few days.

## 385: Webhook signature verification works locally but fails in production. What would you check?

- Is the production secret the one for the production endpoint, not the CLI secret or the staging one?
- Does something change the body before your code? A body parser, a proxy, an API gateway or a framework that parses JSON by default.
- Is the body read as text with the right encoding, not re-serialized?
- Does a load balancer or CDN change or strip the `Stripe-Signature` header?
- Is the server clock correct? A large clock skew makes the timestamp check fail.
- Is a test-mode event sent to a live endpoint or the reverse?

The error message from `constructEvent` usually says whether the signature or the timestamp failed.

## 386: A user's subscription is active in Stripe, but they lost access in your app. What could be wrong?

- A webhook failed or arrived out of order, and your copy shows an old status like `past_due` or `canceled`.
- Your code reads a field that moved in a newer API version, like the period end that moved to subscription items.
- The access check doesn't know the new price ID after a plan change.
- The user has two Stripe customers, and you look at the wrong one.
- A cache didn't refresh.

Quick fix: fetch the subscription and update your copy. Real fix: find which of these happened and add a reconciliation job that catches it next time.

## 387: The payment decline rate suddenly doubled. How do you investigate?

1. Split declines by decline code, card brand, country, payment method and flow. Is it one group or everything?
2. Check if it lines up with a deploy, a Radar rule change or a new marketing campaign.
3. Look for card testing: many small attempts, same IP ranges, many different cards.
4. Check if a change removed data from payments (like billing address or CVC collection).
5. Check Stripe's status page and the card networks for incidents.

Many "decline spikes" are really bots. Others come from a deploy that stopped sending `customer` or changed how cards are saved.

## 388: You see a card testing attack happening right now. What do you do?

- Turn on stricter rate limits and CAPTCHA on the checkout endpoint.
- Add temporary Radar rules, for example block payments under a small amount from new customers, or from the attacking IP ranges.
- Block the IPs or user agents at the edge if there's a clear pattern.
- Stop creating PaymentIntents for unauthenticated visitors if your flow allows.
- Contact Stripe support. They can help and may apply extra protection.

Afterwards, refund any successful test payments to avoid disputes, and make the temporary protections permanent where they make sense.

## 389: A payout is lower than finance expected. How do you explain it?

List the balance transactions in that payout and group them by type: payments, refunds, disputes, fees, transfers to connected accounts, adjustments. Common reasons:

- Refunds or disputes from earlier days were taken from the balance.
- Fees were higher than expected (international cards, conversion, add-on products).
- Some payments aren't available yet and will come in the next payout.
- On Connect, transfers to sellers or negative seller balances.

Stripe's payout reconciliation report shows this per payout and is what finance teams usually use.

## 390: Your dispute rate is rising. What would you do?

1. Look at dispute reasons. "Fraudulent" points to fraud, "not recognized" to a bad statement descriptor, "product not received" or "subscription canceled" to fulfillment or cancellation problems.
2. For fraud: tighten Radar, request 3DS on risky payments, and refund on early fraud warnings.
3. For "not recognized": clearer descriptors, receipts and reminder emails before renewals.
4. For subscriptions: easy cancellation and clear trial-end reminders.
5. Fight disputes you can win with good evidence.

Card networks have monitoring programs with thresholds. Going over them brings fines, so act early.

## 391: Payments get stuck in requires_action and never complete. What could be wrong?

- The front end doesn't handle the next action: for example, it confirms on the server but never calls `stripe.handleNextAction()`.
- A popup or iframe for 3DS is blocked by your CSP or by the browser.
- The `return_url` page doesn't handle the redirect back and leaves the user confused.
- The customer gave up during the bank's verification step.
- On mobile, the redirect back to the app isn't configured.

Look at which payment methods and devices are affected. Then test that exact flow with the 3DS test cards, including the "fail authentication" case.

## 392: After upgrading the API version, invoices are no longer linked to payments in your system. What happened?

Most likely the code read `invoice.payment_intent`, `invoice.charge` or `invoice.subscription`, which were removed in the Basil release. After the upgrade those fields are `undefined`, and the code silently skips linking.

Fix: read payments through the invoice payments list, read the subscription from `invoice.parent.subscription_details.subscription`, and add tests that fail when expected fields are missing. Also check the webhook endpoint's API version, since events may come in the old shape while your code expects the new one, or the other way around.

## 393: An order was fulfilled twice. What would you check?

- Is the fulfillment function idempotent, or does it only check "did I process this event ID"? Different events (for example `checkout.session.completed` and `payment_intent.succeeded`) can both trigger fulfillment for the same order.
- Do the success page and the webhook both fulfill without a shared lock?
- Did two workers handle the same event at once, before either saved the event ID?
- Did someone replay events from the Dashboard or the dead letter queue?

The fix is a guard on the business action itself (order status change with a condition, or a unique fulfillment record), not only on event IDs.

## 394: During a big sale you get many 429 errors from Stripe. What do you do?

In the moment: make sure the SDK retries with backoff, turn off non-essential Stripe calls (syncs, analytics, polling), and serve product and price data from cache.

After: find which calls used the limit. Usually it's not the payments, but extra reads around them (fetching customers, prices and subscriptions on every page). Move those to your own database and webhooks. If you expect a really large event, contact Stripe ahead of time about your expected traffic.

## 395: A customer changed plans five times in one day and their invoice is confusing. How do you prevent this?

Each change created proration lines, so the invoice is full of credits and charges. Options:

- Use `proration_behavior: 'none'` for some changes, or apply downgrades only at period end.
- Limit how often a plan can change (for example once per day), or batch changes.
- Show a preview invoice before every change, so the customer knows what will happen.

For this customer, support can explain the lines, or issue a credit note and a clean invoice if they want a simple one.

## 396: A refund failed. What now?

A refund can fail if the card was closed or the bank rejects it. You get `refund.updated` with `status: 'failed'` and a `failure_reason`, and the money goes back to your Stripe balance.

Contact the customer and pay them another way (bank transfer, store credit), record that in your system, and mark the order accordingly. Don't just retry the same refund, it will fail again. Have a support process ready, because this happens regularly at scale.

## 397: A seller's connected account was disabled, and they have money in their balance. What can the platform do?

Check `requirements.disabled_reason` and `requirements.currently_due`. Usually Stripe needs more information or documents. Send the seller to onboarding to provide them. Once fixed, payouts start again.

If the account was disabled for a policy reason (for example a prohibited business), the platform can't simply move the money elsewhere. Work with Stripe support. In the meantime, stop sending new orders to that seller, so the problem doesn't grow.

## 398: The success page says "paid" but your webhook says the session is unpaid. Why?

For async payment methods, the session completes with `payment_status: 'unpaid'` and the payment finishes later. A success page that only checks "session complete" shows the wrong message. Or the page read the status at a different moment than the webhook.

Use the same logic in both places: check `payment_status`, show "payment processing" when it's `unpaid`, and only treat `paid` (or `no_payment_required`) as done. Then handle `checkout.session.async_payment_succeeded` and `checkout.session.async_payment_failed` for the final result.

## 399: Customers say they don't recognize your charges. What do you change?

- Make the statement descriptor match the brand customers know, not the legal company name.
- Add a dynamic suffix with the product or order number.
- Send clear receipts right after payment, with your brand and support contact.
- For subscriptions, send a reminder before renewals and before trials end.
- Put a support email or phone number on the descriptor's support field in the account settings.

These cut "unrecognized" disputes a lot, and they're cheap to do.

## 400: Your webhook queue keeps growing during peak hours. How do you fix it?

First see why: are workers slow (database, external API calls), failing and retrying, or just too few?

- Scale workers out, and partition the queue so related events stay ordered.
- Make handlers faster: fewer Stripe fetches (use thin events wisely, cache), fewer database round trips.
- Move non-critical work (emails, analytics) to separate queues with lower priority.
- Unsubscribe from event types you don't need.

Also check that the endpoint itself only stores and returns 200, and doesn't do processing inline.

## 401: How would you build a one-click upsell after checkout?

During the first payment, save the payment method with `setup_future_usage: 'on_session'` (or `off_session` if you might charge later without the customer). On the thank-you page, offer the upsell. When the customer clicks "Add", the server creates and confirms a new PaymentIntent with the saved payment method:

```js
await stripe.paymentIntents.create({
  amount: 1900,
  currency: "usd",
  customer: order.customerId,
  payment_method: order.paymentMethodId,
  confirm: true,
  metadata: { orderId: order.id, upsell: "extended-warranty" },
  return_url: "https://example.com/order/complete",
});
```

Handle `requires_action`, since the bank can still ask for authentication. Get clear consent in the UI, or you'll create disputes.

## 402: How would you design payments for a marketplace that splits one order among many sellers?

- Charge the buyer once on the platform with a `transfer_group` per order.
- Store order lines with seller, amount and platform fee.
- After payment succeeds (or after delivery), create a transfer per seller with `source_transaction`.
- For refunds of one line, refund that amount to the buyer and reverse that seller's transfer.
- Keep a ledger of what each seller is owed, and reconcile it with transfers and payouts.

Decide early who is the merchant of record, who handles disputes, and when sellers get paid. Those choices shape the whole design.

## 403: How would you design billing for a SaaS with a trial, per-seat pricing and usage add-ons?

- Products: a plan with a per-seat price, and a metered price for usage.
- Sign-up: Checkout in subscription mode with a 14-day trial, or a no-card trial with `trial_settings` to cancel or pause if no card is added.
- Seats: a daily job sets the seat quantity, with prorations added to the next invoice.
- Usage: meter events sent from your usage pipeline, with unique identifiers.
- Access: local subscription table synced from webhooks, one `hasAccess()` function, and a grace period for `past_due`.
- Self-service: Customer Portal for cards, invoices and cancellations.

Start simple. Most of the complexity is in edge cases, so add them as your real customers need them.

## 404: How would you support custom donation amounts, one-time and monthly?

- One-time: create a PaymentIntent (or a Checkout Session with `price_data`) for the amount the donor picks, after checking it's within your min and max.
- Monthly: create a subscription with `price_data` that has `recurring: { interval: 'month' }` and the chosen amount, or a Price created on the fly for that amount.
- Store donor consent for recurring payments and make cancellation easy.
- Send receipts that meet tax rules for donations in your country.

Watch for card testing, since donation forms with free amounts are a favorite target. Add a minimum amount and bot protection.

## 405: How would you add tips for workers on a Connect platform?

Treat the tip as a separate amount that goes fully to the worker:

- If tips are given at checkout, add the tip to the total and send it in the transfer (no platform fee on the tip part).
- If tips are given after the service, charge the saved card off-session with a new PaymentIntent and a destination for that worker.

Show tips separately in your records and in the worker's earnings, and check tax and legal rules for tips in each country.

## 406: How would you build pre-orders that are charged when the product ships?

1. At pre-order, save the card with a SetupIntent (or Checkout in setup mode) and record the order with its price.
2. When the product ships, charge each order off-session with an idempotency key per order.
3. Handle failures: email the customer to update their card and complete the payment on-session.
4. Process in batches with rate limiting, and track which orders were charged.

Don't authorize at pre-order time if shipping is far away, because authorizations expire in about a week.

## 407: How would you implement a refundable deposit, like for a rental?

If the rental is short (within the authorization window), authorize the deposit with manual capture and cancel it when the item is returned, so no money is actually taken.

For longer rentals, save the card with a SetupIntent and only charge if there's damage, off-session, with clear terms the customer agreed to. Or charge the deposit and refund it at return. That's simpler, but the customer waits days for the refund and you pay fees on the charge.

## 408: How would you handle B2B customers who pay invoices on net-30 terms?

- Subscriptions or invoices with `collection_method: 'send_invoice'` and `days_until_due: 30`.
- Enable bank transfer payment methods on the hosted invoice page, since many companies pay this way.
- Collect tax IDs and billing addresses, and let them add a PO number in custom fields or metadata.
- Automatic reminder emails before and after the due date.
- Your access logic should allow unpaid invoices until the due date plus a grace period.

Large customers may pay outside Stripe; record those with `paid_out_of_band` so reports stay correct.

## 409: Can a mobile app use Stripe to sell digital content?

It depends on app store rules, which change and differ by country. Historically, digital goods used inside an iOS or Android app had to use the store's in-app purchase system, while physical goods and services used outside the app (like rides or food) could use Stripe.

Rules have changed in some regions in recent years, allowing links to external payment pages in some cases. Check the current store guidelines and local laws before deciding, and get it reviewed, since getting it wrong can get the app rejected.

## 410: How would you automate refunds while keeping control?

- Define rules: for example, automatic full refund within 14 days for orders under $50, everything else needs approval.
- Build a refund service that checks the rules, creates the refund with an idempotency key, and logs who or what asked for it.
- Support staff use your admin tool, which calls the same service, instead of refunding in the Dashboard.
- Listen to refund webhooks anyway, to catch refunds made in the Dashboard.
- Report refunds by reason and by person each week.

This prevents both slow refunds (which create disputes) and abuse.

## 411: A company has legal entities in the US, the EU and the UK. How would you set up Stripe?

Usually one Stripe account per entity, so payments settle locally, tax and invoices show the right company, and local rules are met. Stripe Organizations let you manage them together.

In the app: choose the account by the customer's country or contract, store `stripeAccountKey` on each customer, keep a client per account, and have a webhook endpoint per account (or route by `event.account` context and secret). Keep shared things like product catalogs in sync with a script that runs against each account.

## 412: How would you build an internal admin tool for payments?

- Use a restricted key with only the permissions the tool needs (read customers and payments, create refunds).
- Require login with your company SSO, and roles (support vs finance vs admin).
- Log every action with the user, the reason and the Stripe request ID.
- Use your own refund and credit services, so business rules apply.
- Show your data and Stripe data side by side, so support can see order status and payment status together.

Avoid giving many people full Dashboard access when a smaller tool can do the job with clear limits.

## 413: How do you load Stripe.js without slowing down your pages?

Stripe.js is loaded from Stripe's CDN and is not small. Options:

- Load it on payment pages with `loadStripe()`, which adds the script only when called.
- On other pages, load it after the page is interactive. Stripe recommends having it on all pages for better fraud signals, so many sites load it lazily rather than not at all.
- Preconnect to `js.stripe.com` and `api.stripe.com` on pages that lead to checkout.

Measure the effect on your web vitals, and balance fraud signals against speed for your site.

## 414: What can go wrong on the front end, and how do you make checkout robust?

- Stripe.js can fail to load (bad network, strict corporate proxies, some privacy extensions). Catch the error from `loadStripe()` and show a message with another way to pay or contact support.
- The page can be reloaded or opened in two tabs. Reuse the same PaymentIntent for the order.
- The customer can go back after paying. Check the order status when the checkout page loads and redirect to the order page if it's paid.
- Network errors during confirm can hide the result. Check the PaymentIntent status before showing a failure.

## 415: What is special about three-decimal currencies?

Currencies like KWD, BHD, JOD and OMR have three decimal places. For card payments in these currencies, Stripe expects the amount in the smallest unit, and the last digit must be 0. So 5.124 KWD can't be charged; you'd charge 5.120 (amount 5120) or 5.130.

If you support many currencies, keep a table of decimals and rounding rules per currency, and test each one. Assuming two decimals everywhere is one of the most common money bugs.

## 416: How do you handle time and dates in Stripe data?

Stripe timestamps are Unix seconds in UTC. JavaScript uses milliseconds, so multiply by 1000 when you create a `Date`:

```js
const periodEnd = new Date(sub.items.data[0].current_period_end * 1000);
```

Billing is based on exact times, not calendar days in the customer's zone. A subscription that started at 23:30 UTC on the 31st renews based on that time, and months with fewer days are handled by Stripe's rules. When you show dates to users, convert to their time zone. When you compare, stay in UTC.

## 417: Why might a snapshot event not contain the data you need?

Snapshot events include the object as it was, but without expanded fields. So `invoice.paid` has the customer ID, not the customer's email. Line items and other lists can also be cut short in event payloads.

Fetch what you need with `expand` in the handler. This is one more reason the "event as a trigger, then fetch" pattern is common.

## 418: How long can you get past events from the API?

The events list endpoint returns events from the last 30 days. Older events can't be fetched there, although the objects themselves (payments, invoices) stay available.

If you need a long history of changes for auditing, store events yourself as they arrive. For data analysis, use Sigma, Data Pipeline or your own warehouse, not the events API.

## 419: How do you delete a customer in your app without breaking things in Stripe?

Decide the order and what happens to money first:

1. Cancel active subscriptions (with or without prorated refunds, by your policy).
2. Handle open invoices: collect, void, or mark uncollectible.
3. Delete the Stripe Customer, which removes saved payment methods.
4. Mark your user as deleted, keeping the order and payment records you're legally required to keep, with personal data removed where allowed.

Doing step 3 first can leave subscriptions and invoices in odd states, and can fire events your handlers don't expect.

## 420: What payment records should a company keep, and for how long?

Tax and accounting laws usually require keeping invoices, receipts, refunds and payment records for several years (often 5 to 10, depending on the country). Disputes and audits can come long after the payment.

Keep your order and ledger records with links to Stripe IDs, and export Stripe reports regularly instead of relying only on the API. Personal data should be kept only as long as needed, so separate financial records from things like full addresses or logs where you can.

## 421: You inherit a messy Stripe integration. How would you improve it?

1. Map what exists: which flows create payments, which events are handled, which API version and SDK version are used.
2. Add monitoring and a reconciliation report first, so you can see current problems and measure improvements.
3. Fix the dangerous things: missing signature checks, client-provided amounts, no idempotency, fulfillment on redirects.
4. Move all Stripe calls behind one module with tests.
5. Then upgrade the API version, move to current APIs (PaymentIntents, Payment Element, meters) and clean up, one flow at a time.

Don't rewrite everything at once. Payments are a bad place for big-bang changes.

## 422: What do you look for when reviewing payment code?

- Amounts and prices come from the server, in integer minor units, with the right currency.
- Every create call that matters has an idempotency key from a stable operation ID.
- Webhooks verify signatures with the raw body, are idempotent and return quickly.
- Fulfillment happens on reliable signals, not on redirects.
- Errors are handled by type, and unknown outcomes are not treated as failures.
- No secrets or client secrets in logs or the front end.
- Stripe IDs used in requests come from your database for the current user.
- Code works with the pinned API version, without removed fields.

## 423: How would you compare Stripe with other payment providers?

Look at:

- Countries, currencies and local payment methods you need.
- Pricing at your volume, including international, conversion and dispute fees.
- Features: billing, tax, marketplaces, in-person payments.
- Authorization rates in your main markets (ask for data or run a test).
- Developer experience: docs, SDKs, test tools, webhooks.
- Payouts timing, reserves and how they handle risk reviews.
- Support quality and account management at your size.

For most startups developer speed matters most. At large volume, rates and authorization rates start to matter more.

## 424: What is the difference between using Stripe directly and using a merchant of record service?

With Stripe directly, you are the merchant. You handle sales tax and VAT registration and filing, fraud, disputes and compliance, with Stripe's tools helping.

A merchant of record (MoR) service sells your product on your behalf. It is the legal seller, handles global tax collection and filing, disputes and much of the compliance, and pays you the net amount. It costs more per transaction and gives you less control, but saves a lot of work for small teams selling software worldwide. Some MoR services run on top of Stripe.

## 425: What is the Stripe v2 API, and how is it different from v1?

The v2 API lives under `/v2/` and is used for newer products, like Accounts v2 and event destinations. Compared to v1:

- Request bodies are JSON, not form-encoded.
- Events are thin, and the SDK has helpers to parse event notifications and fetch the related object.
- Lists use `next_page_url` style pagination.
- Idempotent retries complete the operation instead of replaying a saved response.

v1 and v2 work side by side. You will use both in the same integration for a while, and the SDK supports both.

## 426: Which Stripe Dashboard settings can change how your code behaves?

- Enabled payment methods and payment method configurations.
- Radar rules.
- Billing settings: retries, what happens after failed payments, invoice finalization.
- Customer Portal configuration.
- Tax registrations and default tax behavior.
- The account's default API version.
- Payout schedule.

Someone can change these without a deploy. Document who owns each one, review changes, and where possible manage them with the API or scripts (for example portal configurations and payment method configurations), so they're versioned like code.

## 427: How do you look up Stripe data quickly when you have millions of customers?

Don't rely on Stripe list or search calls for lookups in your app. Keep your own mapping tables (user to customer, order to PaymentIntent, account to subscription), indexed by both your ID and the Stripe ID.

Webhook handlers then find your records by Stripe ID with one indexed query. For analytics over all customers, use Sigma or a data warehouse fed by Data Pipeline, not the API.

## 428: How do you deploy webhook workers without losing events?

- The endpoint stores events before responding, so a restart only affects events that weren't stored, and Stripe retries those.
- Workers finish their current event on shutdown (handle `SIGTERM`, stop taking new jobs, then exit).
- Jobs are acknowledged only after processing, so a crash returns them to the queue.
- New code must handle events stored by old code and the reverse, for at least one deploy.

With these in place, you can deploy at any time without a "payment freeze".

## 429: How do you roll out a risky change to the payment flow?

- Put the new flow behind a feature flag, and send a small share of traffic to it.
- Compare conversion, authorization rate and errors between old and new.
- Make sure both flows produce the same records in your database, so fulfillment and reporting don't care which one was used.
- Keep the old flow working until the new one is proven, and have a quick switch back.

Avoid releasing payment changes right before peak sales periods.

## 430: You just launched payments. What do you watch in the first week?

- Payment success and decline rates, compared to what you saw in tests.
- Webhook delivery success and processing time.
- Orders stuck between paid and fulfilled.
- Errors in logs from Stripe calls.
- First payouts: do the amounts match your expectations?
- Support tickets about payments.
- Radar blocks and any early disputes or fraud warnings.

Check them daily and have someone ready to fix issues quickly. Small problems in the first week are much cheaper than the same problems a few months in.

## 431: What are the most common mistakes in Stripe integrations?

- Trusting the amount or price from the client.
- Fulfilling on the success redirect instead of webhooks.
- Parsing the webhook body before verifying the signature.
- Not making webhook handlers idempotent.
- Creating a new PaymentIntent or Customer on every page load.
- Treating timeouts as failures and charging again.
- Using floats for money and assuming two decimals everywhere.
- Ignoring async payment methods and `processing`.
- Hardcoding price IDs and fee rates.
- Using fields removed in newer API versions from old tutorials.

## 432: How would you design payment collection for invoices your own system creates?

If your system creates the bills (for example a utility or rental platform), you can still use Stripe for collection:

- Create a Stripe invoice from your bill, with your bill ID in metadata, or a PaymentIntent if you don't need Stripe invoices.
- Charge the saved payment method on the due date, with an idempotency key per bill and attempt.
- On failure, retry on a schedule you control, using the decline code to decide, and email the customer a link to pay.
- Mark the bill paid from webhooks.

Using Stripe Invoicing gives you hosted pages, PDFs and reminders for free. Using bare PaymentIntents gives more control but more work.

## 433: How do you handle refunds from both your admin tool and the Stripe Dashboard?

Treat Stripe as the source of truth for refunds. Your tool creates refunds through the API with an idempotency key, and records a "refund requested" entry. The webhook (`charge.refunded`, `refund.updated`) records the actual refund, no matter where it came from.

Match refunds to your requests by metadata. A refund without metadata came from the Dashboard, so log it and link it to the order through the PaymentIntent. This way, reports are right even when support uses the Dashboard.

## 434: How would you handle partial shipments for an order paid upfront?

Two common approaches:

- Charge the full amount at checkout, and refund items you can't ship.
- Authorize the full amount, capture what ships in the first shipment, and charge the rest later off-session (or authorize again). Note that a PaymentIntent can usually only be captured once, unless your account supports multiple captures.

The first is simpler and works with any payment method. The second avoids charging for things not shipped but is more complex and depends on card support. Many stores pick the first.

## 435: How would you let customers pay with store credit and a card together?

Stripe doesn't split one payment between your store credit and a card. Do it yourself:

1. Calculate how much store credit applies, and reserve it in your ledger.
2. Create a PaymentIntent for the remaining amount only.
3. When the payment succeeds, commit the credit use. If it fails or is canceled, release the reservation.
4. On refunds, decide the order: refund to the card first or to store credit first, and write it in your policy.

If the credit covers everything, skip Stripe and mark the order paid.

## 436: How do you sell add-ons in the middle of a subscription period?

Add a new item to the subscription with prorations:

```js
await stripe.subscriptions.update("sub_123", {
  items: [{ price: "price_addon_storage" }],
  proration_behavior: "always_invoice",
  payment_behavior: "pending_if_incomplete",
});
```

The customer pays the prorated amount now, and from the next period the add-on is part of the normal invoice. With `pending_if_incomplete`, the add-on only becomes active if the payment succeeds, so give access when the update is applied, not when the request is sent.

## 437: How would you show customers their current usage and upcoming bill?

- Usage: use meter event summaries from Stripe for the period (`stripe.billing.meters.listEventSummaries()`), or better, your own usage database, which is faster and can show more detail.
- Upcoming bill: a preview invoice for the subscription, cached for a short time because it's an API call.

Show both clearly with dates. Customers who can see usage grow are much less likely to dispute a large invoice.

## 438: How do you stop people from abusing free trials?

- Require a card for the trial, and use the card fingerprint to allow one trial per card.
- Block prepaid or virtual cards for trials with a Radar rule, if abuse comes from them.
- Check email domains and require email verification.
- Limit trials per device or IP range with your own checks.
- Use a SetupIntent at signup, which checks the card is real.

Balance it against conversion. Strict rules also stop real customers from trying the product.

## 439: How do you protect saved cards if a user's account is taken over?

An attacker who logs in can use saved cards to buy things. Protect against it:

- Ask for re-authentication (password or 2FA) before purchases from new devices, or before changing the email or adding a card.
- Ask for the CVC again for high-value purchases with saved cards.
- Send emails for new payments and new cards.
- Watch for unusual patterns (new country, many orders) and use Radar rules with your account signals in metadata.

## 440: What security issues can come up with Customer Portal and Checkout URLs?

- Portal sessions log the user into their billing. Create them only for the logged-in user's own customer, and don't send them in long-lived emails.
- `return_url` and `success_url` should point to your own domains, not take a URL from the request (open redirect).
- Checkout Session URLs can be shared. Make sure fulfillment links the payment to the right account by your own records, not by who opened the link.
- Don't put personal data in URL parameters.

## 441: In a B2B SaaS, should the Stripe customer be the user or the organization?

Usually the organization (team, workspace, tenant). The organization has the subscription, the billing email, tax ID and invoices. Several users belong to it, and some of them have billing permissions.

Store `stripe_customer_id` on the organization table, and check that the user has a billing role before opening the portal or changing plans. Making each user a customer causes problems as soon as two people from the same company need to manage billing.

## 442: How do tax rate changes affect existing subscriptions?

With Stripe Tax, new invoices use the current rate automatically, based on the customer's location and the product tax code. Invoices already finalized keep their old rate.

If you set tax rates by hand (tax rate objects), you need to create a new rate and update subscriptions to use it, because tax rate objects can't change their percentage. That's one of the main reasons teams move to Stripe Tax.

## 443: How do you test Connect flows?

- Create connected accounts in a sandbox and use Stripe's test data in onboarding (test SSNs, test bank account numbers, test documents) to reach verified or restricted states.
- Use test cards to create payments, refunds and disputes on destination and direct charges.
- Use `stripe listen --forward-connect-to` to get events from connected accounts locally.
- Test payouts and failed payouts with Stripe's test bank account numbers.

Test what your platform does when an account gets restricted, not only the happy path.

## 444: What is Smart Disputes?

Smart Disputes is a Stripe feature that can automatically build and submit evidence for eligible disputes, using data Stripe already has about the payment (and data you've given it, like customer details and receipts).

It saves time for teams with many small disputes. You still need good data on your payments (customer, description, metadata, receipts) for it to work well, and you may want to handle high-value disputes yourself.

## 445: When would you choose Elements over Checkout, even though it's more work?

- The checkout is part of a complex flow, like a multi-step booking or an in-app purchase screen, and a redirect would break it.
- You need full control over the layout and order of fields, or to combine payment with other inputs on one page.
- You want to mix payment with things Checkout doesn't support in your flow.

The costs: more front-end code, more states to handle (3DS, async methods), more PCI care on your page, and you must keep up with Stripe changes yourself. Checkout Sessions with your own Elements-based UI is a middle way that keeps many Checkout features.

## 446: Why should you be careful when one action creates events on both the platform and a connected account?

With destination charges, a payment creates events on the platform (the PaymentIntent) and on the connected account (the transfer and its payment). With direct charges, the events are on the connected account, and the platform gets application fee events.

If you listen to both, you can process the "same" business event twice, or wait for an event that comes to the other destination. Decide which event drives each action, and document it.

## 447: What changed about webhook verification tolerance in the latest Node SDK major version?

In `stripe` v23, the verify helpers use the default tolerance (5 minutes) unless you pass another one, and passing `0` to `constructEvent` turns the timestamp check off.

So code that passed `0` thinking it meant "use the default" now has no replay protection. Don't pass a tolerance unless you have a good reason, and check for this when upgrading the SDK. This is also a good example of why you should read the SDK changelog, not just the API changelog.

## 448: A customer opens Checkout, and you change the price before they pay. What happens?

The Checkout Session uses the price that was set when the session was created. If you archive the price or create a new one, the open session still charges the old amount until it expires.

If prices change often (flash sales, dynamic pricing), create sessions with a short `expires_at`, check the session's amounts in your webhook against your expected price, and decide how to handle the difference, usually by honoring what the customer saw.

## 449: What records should you keep to explain payment decisions to finance or auditors?

- Every order with its amounts, currency, tax and discount breakdown at the time of purchase.
- The link from each order to Stripe objects (PaymentIntent, invoice, refund, dispute).
- Who did what: refunds, credits, plan changes made by staff, with reasons.
- Your reconciliation results and how differences were resolved.
- Policies in force at the time (refund policy, pricing).

If you can't explain a number from your own records, you'll end up doing manual archaeology in the Dashboard during the audit.

## 450: You're the first engineer at a startup that needs to start charging customers. How would you set up payments?

Start simple and leave room to grow:

1. Use Checkout for payments and subscriptions, the Customer Portal for self-service, and Stripe Tax if you sell in many places.
2. Store the Stripe customer ID on the user or organization, and price lookup keys in config.
3. Build one webhook endpoint with signature checks, an events table for idempotency, and handlers that sync subscriptions and orders.
4. Write one `hasAccess()` function based on your synced data.
5. Turn on Smart Retries, receipts and failed payment emails.
6. Add basic monitoring: webhook failures, payment success rate, and a weekly reconciliation check.

Move to Elements, usage billing or Connect only when a real need comes up. Most early payment bugs come from custom code that didn't need to exist.
