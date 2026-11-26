# Scaling an App From 1 to 1 Million Users, Step by Step

▶ **Watch:** https://youtu.be/dht9TtQvCHU

## In the video

1. One box does everything
2. Split, then scale
3. Stateless servers and a load balancer
4. Cache and CDN
5. Replicas, queues and shards
6. Measure, then scale

## Key facts (checked for the video)

- A typical starting point is one server running the web app and the database together. It is simple, but it is a single point of failure, and the app and database compete for the same CPU, memory and disk.
- The first common step is moving the database to its own machine, so the web tier and data tier can be sized and scaled separately.
- Vertical scaling (scale up) means a bigger machine - more CPU, RAM, faster disks. It needs no code changes, but it has a hard ceiling, gets expensive, and is still a single point of failure.
- Horizontal scaling (scale out) means adding more machines and spreading the load across them. It works best when web servers are stateless.
- Stateless web servers keep no user session in local memory; session data lives in a shared store such as Redis or a database, or in a signed cookie or token, so any server can handle any request.
- A load balancer sits in front of the web servers, gives clients one address, spreads requests (for example round robin or least connections), runs health checks, and stops sending traffic to unhealthy servers. The load balancer itself is usually run as a redundant pair or a managed service so it is not a single point of failure.
- A cache such as Redis or Memcached keeps frequently read data in memory, which is much faster than a database query. Cache-aside is the common pattern: read the cache, on a miss read the database and store the result with a TTL.
- Caching brings the hardest problem - invalidation. Data can go stale, so cached entries need expiry times and must be updated or deleted when the underlying data changes.
- A CDN serves static files (images, CSS, JavaScript, video) from edge servers close to users, which cuts latency and removes that traffic from your own servers.
- Database replication - one primary handles writes, one or more read replicas copy its changes and serve reads. Most web apps read far more than they write, so replicas add read capacity and give a failover target.
- Replication is usually asynchronous, so replicas can lag slightly behind the primary; a user may not see their own write immediately if it is read from a replica (replication lag).
- A common way to avoid that is read-your-own-writes - serve a user's own recently changed data from the primary, and other reads from replicas.
- Message queues (for example RabbitMQ, Kafka or SQS) let slow work such as sending emails, resizing images or generating reports run in background workers, so web requests return quickly and spikes are smoothed out.
- Sharding (horizontal partitioning) splits one database's rows across several databases by a shard key such as user ID. It scales writes and storage, but cross-shard queries and joins become hard, and a badly chosen key creates hot shards.
- Monitoring, logging and metrics are needed at every stage to find the real bottleneck before adding more machines; the order of these steps depends on where the bottleneck actually is.
- Avoid inventing user counts per stage: real thresholds depend entirely on the workload, so present the stages as a typical progression, not fixed numbers.
