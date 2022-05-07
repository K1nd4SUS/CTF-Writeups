# Auth Skip

## Description

Clam was doing his angstromCTF flag% speedrun when he ran into [the infamous timesink](https://auth-skip.web.actf.co/) known in the speedrunning community as "auth". Can you pull off the legendary auth skip and get the flag?

[Source](index.js)

## Solution

The only things to do is set a cookie as `user=admin`

```javascript
app.post("/login", (req, res) => {
    if (
        req.body.username !== "admin" ||
        req.body.password !== Math.random().toString()
    ) {
        res.status(401).type("text/plain").send("incorrect login");
    } else {
        res.cookie("user", "admin");
        res.redirect("/");
    }
});
```

#### **FLAG >>** `actf{passwordless_authentication_is_the_new_hip_thing}`