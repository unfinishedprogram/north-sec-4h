There's a forum post. We read through the comments and it seems like we have to connect to an SQL server.

It seems like there's db scripts which answer to "flags". "Flags are key words with specific triggers", says the post.

We connect to the db using the given credentials. It seems like the user we're given doesn't seem to have enough privileges to look at the triggers. We have to query something for "flags" and I think that we might get what we're looking for.

After looking at the current user, we found out that we aren't logged in as "worker" but as "guest"
