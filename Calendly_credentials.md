# How to Obtain Calendly API Credentials

To access the Calendly API and obtain the necessary credentials, you'll need to follow these steps:

## 1. Authentication Token (Auth Token)

1. Visit the [Calendly API Webhooks Integration Page](https://calendly.com/integrations/api_webhooks).

2. Generate an Authentication Token:
   - This token is used to authenticate your requests to the Calendly API.

## 2. Organization URI (Org URI)

To retrieve your organization URI, you can use Postman or any HTTP client. Here's an example using `curl`:

```bash
curl --location 'https://api.calendly.com/users/me' \
--header 'Authorization: Bearer your_auth_token' \
--header 'Cookie: __cf_bm=1jRXXKh5vICx1U57cGsr6yUVP6t5arLZO_EppAmFfZI-1694643576-0-AYrJ671tnPOeZkgYklA2Au0bHjPh2ZOsv0UNLCB7OVXVZBPYv7uARBB5/7NnsD2gccSwQviKed3ViX+hJqIewvQ='
```

Replace `your_auth_token` with the token you generated earlier.

You will receive a response containing your information, including your organization URI.

Example Response:

```json
{
    "resource": {
        "avatar_url": null,
        "created_at": "2023-09-16T23:42:14.368592Z",
        "current_organization": "https://api.calendly.com/organizations/Your_ORG_UUId",
        "email": "example@gmail.com",
        "name": "your-name",
        "resource_type": "User",
        "scheduling_url": "https://calendly.com/your-name",
        "slug": "your-name",
        "timezone": "Africa/Lagos",
        "updated_at": "2023-09-13T21:46:08.109069Z",
        "uri": "https://api.calendly.com/users/your_user_ID"
    }
}
```

- The "current_organization" field in the response contains the URL of your organization (`https://api.calendly.com/organizations/Your_ORG_UUId`).

With these credentials, you can now access the Calendly API and perform various operations, such as creating events or retrieving scheduling data. Make sure to keep your authentication token secure, as it provides access to your Calendly account.
