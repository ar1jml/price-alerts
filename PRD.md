# Price Alerts — Product Requirements Document

**Status:** Early development  
**Document scope:** Proposed product requirements; features marked planned are not implemented yet.

## 1. Product overview

Price Alerts is intended to help shoppers track the prices of products they are considering. A user adds a product, chooses a target price, and receives useful information when the price changes or reaches that target.

## 2. Problem and goals

Shoppers often revisit product pages to check prices and may miss a favorable price change. Price Alerts aims to:

- Reduce repetitive manual price checks.
- Help users compare current prices with their own target prices.
- Provide understandable price history for tracked products.
- Notify users when a configured price condition is met.

Price Alerts is an informational tool. It does not purchase products on a user's behalf or guarantee that a displayed price remains available.

## 3. Users

- **Price-conscious shopper:** wants to follow a product and buy when its price is acceptable.
- **Frequent online shopper:** wants a single place to review multiple tracked products.

## 4. Scope and implementation status

| Capability | Status |
| --- | --- |
| Register an account | Implemented in the backend |
| Log in and receive a JWT access token | Implemented in the backend |
| Connect the Vue login UI to the backend | Planned |
| Add and manage tracked products | Planned |
| Set a target price per product | Planned |
| Store and display price history | Planned |
| Check product prices on a schedule | Planned |
| Notify users when a target is reached | Planned |

## 5. Functional requirements

### Accounts

- Registration accepts an email and password.
- Email addresses must be unique.
- Passwords must meet the API's minimum length requirement.
- Login verifies the supplied password against the stored password hash.
- Invalid login attempts return a generic authentication error.
- Successful login returns a signed, expiring access token.

### Product tracking — planned

- A signed-in user can add a supported product URL.
- A user can set, update, pause, or remove a target price.
- Product and alert data are private to the owning user.
- Unsupported or invalid product URLs receive a clear validation error.

### Price history and notifications — planned

- Price checks are recorded with their observation time.
- Users can review changes for a tracked product.
- A notification is sent when a configured target condition is met.
- A notification should identify the product, observed price, and observation time.

## 6. Non-functional requirements

- Never store plaintext passwords.
- Keep secrets and database credentials out of tracked source files.
- Validate input at the API boundary and return appropriate HTTP status codes.
- Avoid exposing one user's products or alerts to another user.
- Make background price-check failures observable and retryable.
- Clearly indicate when price data was last checked; do not imply prices are guaranteed current.

## 7. Initial acceptance criteria

1. A user can register with a valid email and password.
2. Re-registering an existing email returns a conflict response.
3. Correct credentials return an access token; incorrect credentials return `401`.
4. A user can create a product watch with a URL and target price. **Planned.**
5. A target-price condition can trigger a user notification. **Planned.**
6. Users cannot access another user's watches or alerts. **Planned.**

## 8. Success measures

Once product tracking is implemented, evaluate:

- Number of active tracked products per user.
- Percentage of scheduled price checks completed successfully.
- Time between observing a target price and issuing its notification.
- User retention and notification usefulness.

Set numeric targets after collecting a baseline; no targets are assumed in this document.

## 9. Open product decisions

- Which stores and product URL formats are supported first?
- How frequently should products be checked, and what are the provider limits?
- Which notification channels are required for the first release?
- What should happen when a store blocks or changes its product page?
- Should users choose currency, locale, and notification quiet hours?
