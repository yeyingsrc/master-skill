# Track 02 — Tools (software architecture)

> Wave 2 Track 02 — 10 大类工具地图 + 中国本土 Apache 顶级项目补充. Industry: software architecture, locale=global (国际 + 中国本土并重), profile=practitioner.
>
> 结构约束 notes (诚实): (1) 工具栈 hype 周期 6-12 月 — Service Mesh (2018-2020 hype, 2022+ 'often unnecessary') / Web3 / Blockchain / Serverless / "AI 架构" 2024-2026 当前 hype 高点, 6-9 月 decay 必须标 `last_updated`; (2) 大厂选型 ≠ 中小公司选型 — Stack Overflow / Shopify / Basecamp 公开 case study 反复证明 'modular monolith + PostgreSQL + Redis + 1 台 ECS' 在 < 50 服务时 比 K8s + Istio + Kafka 经济; (3) 中国本土 Apache 顶级项目 (Dubbo / RocketMQ / SkyWalking / APISIX 已毕业) 是中国架构事实标准, 不是 "国际栈替代品" 而是 "中国大厂规模本土实践", 国外团队同样使用; (4) 国产化替代浪潮 (国密 / 等保 / 信创) 让 OceanBase / TDSQL / GaussDB / TDengine / OpenGauss 在政府 + 金融场景大量替代 Oracle / MySQL; (5) AI 辅助架构 (Copilot / Cursor / Claude Code) 2024-2026 是 productivity boost 但不替代设计判断 — 反例: 不靠 LLM 决定 service boundary 或 polyglot persistence 选型; (6) observability vendor 选型 (Honeycomb vs Datadog vs Grafana stack) 有商业拉锯, 不背书单一.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.drawio.com/ | surrogate_primary | 2026-05-17 | JGraph (drawio) | vendor docs — diagrams.net official site |
| T02-S002 | https://github.com/jgraph/drawio | surrogate_primary | 2026-05-17 | JGraph GitHub | vendor docs — drawio open source repo |
| T02-S003 | https://www.lucidchart.com/pages | surrogate_primary | 2026-05-17 | Lucid Software | vendor docs (供应商) |
| T02-S004 | https://excalidraw.com/ | surrogate_primary | 2026-05-17 | Excalidraw | vendor docs — hand-drawn whiteboard tool |
| T02-S005 | https://github.com/excalidraw/excalidraw | surrogate_primary | 2026-05-17 | Excalidraw GitHub | vendor docs — open source repo |
| T02-S006 | https://miro.com/ | surrogate_primary | 2026-05-17 | Miro | vendor docs (供应商) |
| T02-S007 | https://www.figma.com/figjam/ | surrogate_primary | 2026-05-17 | Figma | vendor docs (供应商) |
| T02-S008 | https://whimsical.com/ | surrogate_primary | 2026-05-17 | Whimsical | vendor docs (供应商) |
| T02-S009 | https://www.eraser.io/ | surrogate_primary | 2026-05-17 | Eraser | vendor docs (供应商) |
| T02-S010 | https://c4model.com/ | surrogate_primary | 2026-05-17 | Simon Brown | vendor docs (Simon Brown 一手) — C4 model spec |
| T02-S011 | https://structurizr.com/ | surrogate_primary | 2026-05-17 | Simon Brown / Structurizr Ltd | vendor docs (Simon Brown 一手) |
| T02-S012 | https://docs.structurizr.com/dsl | surrogate_primary | 2026-05-17 | Structurizr | vendor docs — Structurizr DSL ref |
| T02-S013 | https://plantuml.com/ | surrogate_primary | 2026-05-17 | PlantUML | vendor docs |
| T02-S014 | https://mermaid.js.org/ | surrogate_primary | 2026-05-17 | Mermaid | vendor docs |
| T02-S015 | https://github.com/mermaid-js/mermaid | surrogate_primary | 2026-05-17 | Mermaid GitHub | vendor docs — repo + GitHub Markdown native render |
| T02-S016 | https://d2lang.com/ | surrogate_primary | 2026-05-17 | Terrastruct | vendor docs — D2 declarative diagram lang |
| T02-S017 | https://icepanel.io/ | surrogate_primary | 2026-05-17 | IcePanel | vendor docs (供应商) — collaborative C4 model tool |
| T02-S018 | https://github.com/npryce/adr-tools | surrogate_primary | 2026-05-17 | Nat Pryce | vendor docs — adr-tools original Nygard-inspired CLI |
| T02-S019 | https://adr.github.io/ | surrogate_primary | 2026-05-17 | ADR GitHub org | vendor docs — Architecture Decision Records collective home |
| T02-S020 | https://github.com/thomvaill/log4brains | surrogate_primary | 2026-05-17 | Thomvaill | vendor docs — log4brains ADR static-site generator |
| T02-S021 | https://github.com/mrwilson/adr-viewer | surrogate_primary | 2026-05-17 | Mr Wilson | vendor docs — adr-viewer static viewer |
| T02-S022 | https://www.openapis.org/ | surrogate_primary | 2026-05-17 | OpenAPI Initiative | vendor docs (spec 一手) |
| T02-S023 | https://swagger.io/specification/ | surrogate_primary | 2026-05-17 | SmartBear Swagger | vendor docs (spec 一手) |
| T02-S024 | https://stoplight.io/ | surrogate_primary | 2026-05-17 | Stoplight (SmartBear) | vendor docs (供应商) |
| T02-S025 | https://www.postman.com/ | surrogate_primary | 2026-05-17 | Postman | vendor docs (供应商) |
| T02-S026 | https://www.usebruno.com/ | surrogate_primary | 2026-05-17 | Bruno | vendor docs — open source API client, git-friendly |
| T02-S027 | https://github.com/usebruno/bruno | surrogate_primary | 2026-05-17 | Bruno GitHub | vendor docs |
| T02-S028 | https://insomnia.rest/ | surrogate_primary | 2026-05-17 | Kong | vendor docs (供应商) |
| T02-S029 | https://hoppscotch.io/ | surrogate_primary | 2026-05-17 | Hoppscotch | vendor docs — open source web-based API client |
| T02-S030 | https://graphql.org/ | surrogate_primary | 2026-05-17 | GraphQL Foundation | vendor docs (spec 一手) |
| T02-S031 | https://www.apollographql.com/docs/federation/ | surrogate_primary | 2026-05-17 | Apollo | vendor docs (供应商) — Apollo Federation |
| T02-S032 | https://hasura.io/ | surrogate_primary | 2026-05-17 | Hasura | vendor docs (供应商) |
| T02-S033 | https://www.graphile.org/postgraphile/ | surrogate_primary | 2026-05-17 | Graphile | vendor docs |
| T02-S034 | https://grpc.io/ | surrogate_primary | 2026-05-17 | gRPC (CNCF) | vendor docs (spec 一手) |
| T02-S035 | https://buf.build/ | surrogate_primary | 2026-05-17 | Buf | vendor docs (供应商) — protobuf tooling |
| T02-S036 | https://www.asyncapi.com/ | surrogate_primary | 2026-05-17 | AsyncAPI Initiative | vendor docs (spec 一手) |
| T02-S037 | https://kafka.apache.org/ | surrogate_primary | 2026-05-17 | Apache Kafka | vendor docs |
| T02-S038 | https://kafka.apache.org/documentation/ | surrogate_primary | 2026-05-17 | Apache Kafka | vendor docs |
| T02-S039 | https://www.confluent.io/product/confluent-platform/ | surrogate_primary | 2026-05-17 | Confluent | vendor docs (供应商) — Schema Registry + Connect |
| T02-S040 | https://pulsar.apache.org/ | surrogate_primary | 2026-05-17 | Apache Pulsar | vendor docs |
| T02-S041 | https://www.rabbitmq.com/ | surrogate_primary | 2026-05-17 | Broadcom RabbitMQ | vendor docs (供应商) |
| T02-S042 | https://nats.io/ | surrogate_primary | 2026-05-17 | Synadia NATS | vendor docs — CNCF graduated |
| T02-S043 | https://redpanda.com/ | surrogate_primary | 2026-05-17 | Redpanda Data | vendor docs (供应商) — Kafka-API compatible C++ broker |
| T02-S044 | https://aws.amazon.com/sqs/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S045 | https://aws.amazon.com/sns/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S046 | https://cloud.google.com/pubsub | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs (供应商) |
| T02-S047 | https://learn.microsoft.com/azure/service-bus-messaging/ | surrogate_primary | 2026-05-17 | Microsoft | vendor docs (供应商) |
| T02-S048 | https://flink.apache.org/ | surrogate_primary | 2026-05-17 | Apache Flink | vendor docs |
| T02-S049 | https://kafka.apache.org/documentation/streams/ | surrogate_primary | 2026-05-17 | Apache Kafka | vendor docs — Kafka Streams |
| T02-S050 | https://ksqldb.io/ | surrogate_primary | 2026-05-17 | Confluent | vendor docs (供应商) |
| T02-S051 | https://materialize.com/ | surrogate_primary | 2026-05-17 | Materialize | vendor docs (供应商) |
| T02-S052 | https://www.risingwave.com/ | surrogate_primary | 2026-05-17 | RisingWave | vendor docs (供应商) — streaming SQL |
| T02-S053 | https://debezium.io/ | surrogate_primary | 2026-05-17 | Red Hat / Debezium | vendor docs — CDC platform |
| T02-S054 | https://beam.apache.org/ | surrogate_primary | 2026-05-17 | Apache Beam | vendor docs |
| T02-S055 | https://istio.io/ | surrogate_primary | 2026-05-17 | Istio (CNCF) | vendor docs |
| T02-S056 | https://linkerd.io/ | surrogate_primary | 2026-05-17 | Buoyant / Linkerd (CNCF) | vendor docs |
| T02-S057 | https://www.consul.io/docs/connect | surrogate_primary | 2026-05-17 | HashiCorp | vendor docs (供应商) — Consul Connect |
| T02-S058 | https://cilium.io/ | surrogate_primary | 2026-05-17 | Isovalent / Cilium (CNCF) | vendor docs — eBPF networking + mesh |
| T02-S059 | https://www.envoyproxy.io/ | surrogate_primary | 2026-05-17 | Envoy (CNCF) | vendor docs |
| T02-S060 | https://konghq.com/ | surrogate_primary | 2026-05-17 | Kong | vendor docs (供应商) |
| T02-S061 | https://tyk.io/ | surrogate_primary | 2026-05-17 | Tyk | vendor docs (供应商) |
| T02-S062 | https://apisix.apache.org/ | surrogate_primary | 2026-05-17 | Apache APISIX (支流科技) | vendor docs |
| T02-S063 | https://traefik.io/traefik/ | surrogate_primary | 2026-05-17 | Traefik Labs | vendor docs (供应商) |
| T02-S064 | https://aws.amazon.com/api-gateway/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S065 | https://cloud.google.com/apigee | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs (供应商) |
| T02-S066 | https://kubernetes.io/ | surrogate_primary | 2026-05-17 | Kubernetes (CNCF) | vendor docs |
| T02-S067 | https://kubernetes.io/releases/ | surrogate_primary | 2026-05-17 | Kubernetes (CNCF) | vendor docs — 1.36 released 2026-05 |
| T02-S068 | https://www.nomadproject.io/ | surrogate_primary | 2026-05-17 | HashiCorp | vendor docs (供应商) |
| T02-S069 | https://aws.amazon.com/ecs/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S070 | https://cloud.google.com/run | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs (供应商) |
| T02-S071 | https://learn.microsoft.com/azure/container-apps/ | surrogate_primary | 2026-05-17 | Microsoft | vendor docs (供应商) |
| T02-S072 | https://fly.io/docs/machines/ | surrogate_primary | 2026-05-17 | Fly.io | vendor docs (供应商) |
| T02-S073 | https://render.com/ | surrogate_primary | 2026-05-17 | Render | vendor docs (供应商) |
| T02-S074 | https://railway.app/ | surrogate_primary | 2026-05-17 | Railway | vendor docs (供应商) |
| T02-S075 | https://helm.sh/ | surrogate_primary | 2026-05-17 | Helm (CNCF) | vendor docs |
| T02-S076 | https://kustomize.io/ | surrogate_primary | 2026-05-17 | Kustomize | vendor docs — Kubernetes SIG-CLI |
| T02-S077 | https://www.crossplane.io/ | surrogate_primary | 2026-05-17 | Crossplane (CNCF) | vendor docs — control-plane for cloud APIs |
| T02-S078 | https://www.postgresql.org/ | surrogate_primary | 2026-05-17 | PostgreSQL Global Dev Group | vendor docs — PG 18.4 released 2026-05-14 |
| T02-S079 | https://www.mysql.com/ | surrogate_primary | 2026-05-17 | Oracle MySQL | vendor docs (供应商) |
| T02-S080 | https://mariadb.org/ | surrogate_primary | 2026-05-17 | MariaDB Foundation | vendor docs |
| T02-S081 | https://www.sqlite.org/ | surrogate_primary | 2026-05-17 | SQLite | vendor docs |
| T02-S082 | https://www.cockroachlabs.com/ | surrogate_primary | 2026-05-17 | Cockroach Labs | vendor docs (供应商) |
| T02-S083 | https://www.pingcap.com/tidb/ | surrogate_primary | 2026-05-17 | PingCAP | vendor docs (供应商) — TiDB HTAP NewSQL |
| T02-S084 | https://www.yugabyte.com/ | surrogate_primary | 2026-05-17 | Yugabyte | vendor docs (供应商) |
| T02-S085 | https://cloud.google.com/spanner | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs (供应商) |
| T02-S086 | https://aws.amazon.com/rds/aurora/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S087 | https://vitess.io/ | surrogate_primary | 2026-05-17 | Vitess (CNCF) | vendor docs — YouTube origin, MySQL horizontal scaling |
| T02-S088 | https://www.mongodb.com/ | surrogate_primary | 2026-05-17 | MongoDB Inc | vendor docs (供应商) |
| T02-S089 | https://aws.amazon.com/dynamodb/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S090 | https://cassandra.apache.org/ | surrogate_primary | 2026-05-17 | Apache Cassandra | vendor docs |
| T02-S091 | https://www.scylladb.com/ | surrogate_primary | 2026-05-17 | ScyllaDB | vendor docs (供应商) — C++ Cassandra-compatible |
| T02-S092 | https://redis.io/ | surrogate_primary | 2026-05-17 | Redis Ltd | vendor docs (供应商) |
| T02-S093 | https://www.couchbase.com/ | surrogate_primary | 2026-05-17 | Couchbase | vendor docs (供应商) |
| T02-S094 | https://neo4j.com/ | surrogate_primary | 2026-05-17 | Neo4j | vendor docs (供应商) |
| T02-S095 | https://dgraph.io/ | surrogate_primary | 2026-05-17 | Dgraph Labs | vendor docs (供应商) |
| T02-S096 | https://www.elastic.co/elasticsearch | surrogate_primary | 2026-05-17 | Elastic | vendor docs (供应商) |
| T02-S097 | https://opensearch.org/ | surrogate_primary | 2026-05-17 | OpenSearch (AWS-led) | vendor docs |
| T02-S098 | https://www.meilisearch.com/ | surrogate_primary | 2026-05-17 | Meilisearch | vendor docs (供应商) |
| T02-S099 | https://typesense.org/ | surrogate_primary | 2026-05-17 | Typesense | vendor docs (供应商) |
| T02-S100 | https://clickhouse.com/ | surrogate_primary | 2026-05-17 | ClickHouse Inc | vendor docs (供应商) |
| T02-S101 | https://duckdb.org/ | surrogate_primary | 2026-05-17 | DuckDB Foundation | vendor docs — embedded OLAP |
| T02-S102 | https://www.starrocks.io/ | surrogate_primary | 2026-05-17 | StarRocks | vendor docs (供应商) |
| T02-S103 | https://doris.apache.org/ | surrogate_primary | 2026-05-17 | Apache Doris | vendor docs |
| T02-S104 | https://www.snowflake.com/ | surrogate_primary | 2026-05-17 | Snowflake | vendor docs (供应商) |
| T02-S105 | https://cloud.google.com/bigquery | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs (供应商) |
| T02-S106 | https://aws.amazon.com/redshift/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S107 | https://www.databricks.com/ | surrogate_primary | 2026-05-17 | Databricks | vendor docs (供应商) |
| T02-S108 | https://druid.apache.org/ | surrogate_primary | 2026-05-17 | Apache Druid | vendor docs |
| T02-S109 | https://pinot.apache.org/ | surrogate_primary | 2026-05-17 | Apache Pinot | vendor docs |
| T02-S110 | https://opentelemetry.io/ | surrogate_primary | 2026-05-17 | OpenTelemetry (CNCF) | vendor docs — vendor-neutral observability standard |
| T02-S111 | https://www.jaegertracing.io/ | surrogate_primary | 2026-05-17 | Jaeger (CNCF) | vendor docs |
| T02-S112 | https://zipkin.io/ | surrogate_primary | 2026-05-17 | Zipkin | vendor docs |
| T02-S113 | https://prometheus.io/ | surrogate_primary | 2026-05-17 | Prometheus (CNCF) | vendor docs |
| T02-S114 | https://grafana.com/ | surrogate_primary | 2026-05-17 | Grafana Labs | vendor docs (供应商) |
| T02-S115 | https://grafana.com/oss/loki/ | surrogate_primary | 2026-05-17 | Grafana Labs | vendor docs (供应商) — Loki logs |
| T02-S116 | https://www.honeycomb.io/ | surrogate_primary | 2026-05-17 | Honeycomb | vendor docs (供应商) — Charity Majors |
| T02-S117 | https://www.datadoghq.com/ | surrogate_primary | 2026-05-17 | Datadog | vendor docs (供应商) |
| T02-S118 | https://newrelic.com/ | surrogate_primary | 2026-05-17 | New Relic | vendor docs (供应商) |
| T02-S119 | https://www.splunk.com/ | surrogate_primary | 2026-05-17 | Splunk (Cisco) | vendor docs (供应商) |
| T02-S120 | https://www.dynatrace.com/ | surrogate_primary | 2026-05-17 | Dynatrace | vendor docs (供应商) |
| T02-S121 | https://sentry.io/ | surrogate_primary | 2026-05-17 | Sentry | vendor docs (供应商) |
| T02-S122 | https://skywalking.apache.org/ | surrogate_primary | 2026-05-17 | Apache SkyWalking (吴晟) | vendor docs — 国产 APM, Apache 顶级 |
| T02-S123 | https://grafana.com/oss/pyroscope/ | surrogate_primary | 2026-05-17 | Grafana Labs | vendor docs (供应商) — continuous profiling |
| T02-S124 | https://www.polarsignals.com/ | surrogate_primary | 2026-05-17 | Polar Signals | vendor docs (供应商) — Parca cloud |
| T02-S125 | https://www.parca.dev/ | surrogate_primary | 2026-05-17 | Parca | vendor docs — open source continuous profiling |
| T02-S126 | https://github.com/google/pprof | surrogate_primary | 2026-05-17 | Google | vendor docs — Go pprof |
| T02-S127 | https://github.com/Netflix/chaosmonkey | surrogate_primary | 2026-05-17 | Netflix | vendor docs — Chaos Monkey origin |
| T02-S128 | https://chaos-mesh.org/ | surrogate_primary | 2026-05-17 | Chaos Mesh (CNCF, PingCAP) | vendor docs |
| T02-S129 | https://litmuschaos.io/ | surrogate_primary | 2026-05-17 | LitmusChaos (CNCF) | vendor docs |
| T02-S130 | https://www.gremlin.com/ | surrogate_primary | 2026-05-17 | Gremlin | vendor docs (供应商) |
| T02-S131 | https://aws.amazon.com/fis/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) — Fault Injection Service |
| T02-S132 | https://k6.io/ | surrogate_primary | 2026-05-17 | Grafana Labs | vendor docs (供应商) — load test in Go/JS |
| T02-S133 | https://locust.io/ | surrogate_primary | 2026-05-17 | Locust | vendor docs |
| T02-S134 | https://www.artillery.io/ | surrogate_primary | 2026-05-17 | Artillery | vendor docs (供应商) |
| T02-S135 | https://jmeter.apache.org/ | surrogate_primary | 2026-05-17 | Apache JMeter | vendor docs |
| T02-S136 | https://gatling.io/ | surrogate_primary | 2026-05-17 | Gatling | vendor docs (供应商) |
| T02-S137 | https://github.com/tsenart/vegeta | surrogate_primary | 2026-05-17 | Tomás Senart | vendor docs — Vegeta HTTP load tester |
| T02-S138 | https://launchdarkly.com/ | surrogate_primary | 2026-05-17 | LaunchDarkly | vendor docs (供应商) |
| T02-S139 | https://statsig.com/ | surrogate_primary | 2026-05-17 | Statsig | vendor docs (供应商) |
| T02-S140 | https://www.growthbook.io/ | surrogate_primary | 2026-05-17 | GrowthBook | vendor docs — open source feature flags |
| T02-S141 | https://www.getunleash.io/ | surrogate_primary | 2026-05-17 | Unleash | vendor docs |
| T02-S142 | https://www.archunit.org/ | surrogate_primary | 2026-05-17 | ArchUnit | vendor docs — JVM arch tests |
| T02-S143 | https://github.com/BenMorris/NetArchTest | surrogate_primary | 2026-05-17 | Ben Morris | vendor docs — .NET equivalent |
| T02-S144 | https://docs.konsist.lemonappdev.com/ | surrogate_primary | 2026-05-17 | LemonAppDev | vendor docs — Kotlin arch testing |
| T02-S145 | https://docs.openrewrite.org/ | surrogate_primary | 2026-05-17 | Moderne | vendor docs (供应商) — large-scale automated refactoring |
| T02-S146 | https://semgrep.dev/ | surrogate_primary | 2026-05-17 | Semgrep | vendor docs (供应商) — pattern-based static analysis |
| T02-S147 | https://github.com/features/copilot | surrogate_primary | 2026-05-17 | GitHub (Microsoft) | vendor docs (供应商) |
| T02-S148 | https://www.cursor.com/ | surrogate_primary | 2026-05-17 | Anysphere | vendor docs (供应商) — AI-native IDE |
| T02-S149 | https://www.anthropic.com/claude-code | surrogate_primary | 2026-05-17 | Anthropic | vendor docs (供应商) — Claude Code CLI |
| T02-S150 | https://aider.chat/ | surrogate_primary | 2026-05-17 | Paul Gauthier | vendor docs — Aider AI coding CLI |
| T02-S151 | https://codeium.com/ | surrogate_primary | 2026-05-17 | Codeium / Windsurf | vendor docs (供应商) |
| T02-S152 | https://backstage.io/ | surrogate_primary | 2026-05-17 | Spotify (CNCF) | vendor docs — developer portal |
| T02-S153 | https://docusaurus.io/ | surrogate_primary | 2026-05-17 | Meta | vendor docs (供应商) |
| T02-S154 | https://squidfunk.github.io/mkdocs-material/ | surrogate_primary | 2026-05-17 | Martin Donath | vendor docs — MkDocs Material |
| T02-S155 | https://www.terraform.io/ | surrogate_primary | 2026-05-17 | HashiCorp | vendor docs (供应商) |
| T02-S156 | https://opentofu.org/ | surrogate_primary | 2026-05-17 | OpenTofu (Linux Foundation) | vendor docs — Terraform OSS fork |
| T02-S157 | https://www.pulumi.com/ | surrogate_primary | 2026-05-17 | Pulumi | vendor docs (供应商) |
| T02-S158 | https://aws.amazon.com/cdk/ | surrogate_primary | 2026-05-17 | AWS | vendor docs (供应商) |
| T02-S159 | https://dubbo.apache.org/ | surrogate_primary | 2026-05-17 | Apache Dubbo (阿里) | vendor docs — 3.3.6 released 2024-10 |
| T02-S160 | https://github.com/apache/dubbo | surrogate_primary | 2026-05-17 | Apache Dubbo GitHub | vendor docs |
| T02-S161 | https://rocketmq.apache.org/ | surrogate_primary | 2026-05-17 | Apache RocketMQ (阿里) | vendor docs — 5.5.0 released 2025-04 |
| T02-S162 | https://github.com/apache/rocketmq | surrogate_primary | 2026-05-17 | Apache RocketMQ GitHub | vendor docs |
| T02-S163 | https://shardingsphere.apache.org/ | surrogate_primary | 2026-05-17 | Apache ShardingSphere (京东 / 张亮) | vendor docs |
| T02-S164 | https://nacos.io/ | surrogate_primary | 2026-05-17 | Nacos (阿里) | vendor docs — service discovery + config |
| T02-S165 | https://sentinelguard.io/ | surrogate_primary | 2026-05-17 | Sentinel (阿里) | vendor docs — flow control + circuit breaking |
| T02-S166 | https://seata.apache.org/ | surrogate_primary | 2026-05-17 | Apache Seata (阿里) | vendor docs — distributed transactions |
| T02-S167 | https://tdengine.com/ | surrogate_primary | 2026-05-17 | TDengine (涛思) | vendor docs (供应商) — 国产时序库 |
| T02-S168 | https://www.sofastack.tech/ | surrogate_primary | 2026-05-17 | 蚂蚁集团 SOFAStack | vendor docs (供应商) |
| T02-S169 | https://github.com/sofastack/sofa-boot | surrogate_primary | 2026-05-17 | SOFAStack GitHub | vendor docs |
| T02-S170 | https://github.com/mosn/mosn | surrogate_primary | 2026-05-17 | 蚂蚁 MOSN | vendor docs — Go service mesh data plane |
| T02-S171 | https://tarscloud.org/ | surrogate_primary | 2026-05-17 | 腾讯 TARS (Linux Foundation) | vendor docs |
| T02-S172 | https://www.oceanbase.com/ | surrogate_primary | 2026-05-17 | OceanBase (蚂蚁) | vendor docs (供应商) — NewSQL HTAP |
| T02-S173 | https://github.com/oceanbase/oceanbase | surrogate_primary | 2026-05-17 | OceanBase GitHub | vendor docs |
| T02-S174 | https://www.cncf.io/projects/ | surrogate_primary | 2026-05-17 | CNCF | 协会 (CNCF) — graduated + incubating registry |
| T02-S175 | https://projects.apache.org/ | surrogate_primary | 2026-05-17 | Apache 基金会 | 协会 (Apache 基金会) |
| T02-S176 | https://samnewman.io/talks/ | surrogate_primary | 2026-05-17 | Sam Newman personal | vendor docs (作者一手) — "Don't blindly adopt service mesh" |
| T02-S177 | https://world.hey.com/dhh/we-have-left-the-cloud-251760fb | surrogate_primary | 2026-05-17 | DHH (Basecamp/37signals) | vendor docs (作者一手) — leaving the cloud case study |
| T02-S178 | https://shopify.engineering/shopify-monolith | surrogate_primary | 2026-05-17 | Shopify Engineering | vendor docs — modular monolith case |
| T02-S179 | https://stackoverflow.blog/2016/02/17/stack-overflow-the-architecture-2016-edition/ | surrogate_primary | 2026-05-17 | Stack Overflow | vendor docs — SO runs on 9 servers, SQL Server + Redis |
| T02-S180 | https://github.com/getsentry/sentry | surrogate_primary | 2026-05-17 | Sentry GitHub | vendor docs |

---

## 2.1 Diagramming / 系统设计 草图

- **draw.io / diagrams.net** (JGraph, UK). 何时用: 免费 desktop + web, 单文件 .drawio (XML) 可入 git, 适合 ad-hoc 系统图 / 部署拓扑 / AWS-icon 图. Trade-off vs Lucidchart: drawio 完全免费 + 本地优先, Lucidchart 协作更强但商业付费. 默认推荐起点. [T02-S001] [T02-S002] last_updated: 2026 active.

- **Lucidchart** (Lucid Software, Utah). 何时用: 企业团队 multi-user 实时协作画 ERD / BPMN / AWS reference architecture, 与 Confluence/Jira 深度集成. Trade-off: SaaS 锁定 + 中国大陆访问慢, 国内团队多用 draw.io 替代. [T02-S003] last_updated: 2026 active.

- **Excalidraw** (Excalidraw team, open source). 何时用: 手绘风白板, 适合临时讨论 / 演讲 PPT / 架构 brainstorm; .excalidraw JSON 可入 git, VS Code 插件可在 repo 内嵌. Trade-off: 不适合精细 ERD / 部署拓扑, 输出粗糙是 feature 而非 bug. [T02-S004] [T02-S005] last_updated: 2026 active.

- **Miro / FigJam / Whimsical** (SaaS). 何时用: 远程团队 brainstorm / event storming / 团队拓扑 mapping; Miro 模板生态最大, FigJam 与 Figma design system 同源, Whimsical 偏轻量 sticky-notes. Trade-off vs Excalidraw: SaaS 强协作但贵 + 离线弱. [T02-S006] [T02-S007] [T02-S008] last_updated: 2026 active.

- **Eraser** (Eraser, AI-native). 何时用: docs+diagrams 一体, 支持 prompt 生成图 (AI diagram), 适合 Notion-style spec 中嵌图. Trade-off: 较新 (2022+), 团队成熟度不如 draw.io. [T02-S009] last_updated: 2026 active.

## 2.2 Architecture-as-code + ADR

- **C4 Model** (Simon Brown, 2006-). 不是工具是 *notation*: System Context → Container → Component → Code, 4 层 zoom-in 抽象. 几乎所有 architecture-as-code 工具 (Structurizr / IcePanel / Likeable Diagrams) 都基于 C4. [T02-S010] last_updated: 2026 active (Simon Brown 持续 maintain).

- **Structurizr** (Simon Brown). 何时用: C4 DSL (.dsl 文本) → 多视图 (Context / Container / Component) 一处定义多视图生成; Structurizr Lite (Docker 本地) 免费, Structurizr Cloud 付费. 推荐: 团队认可 C4 + 想 diagram 入 git 的首选. Trade-off vs PlantUML: Structurizr 强制 C4 模型一致性, PlantUML 自由但易乱. [T02-S011] [T02-S012] last_updated: 2026 active.

- **PlantUML** (Arnaud Roques). 何时用: 文本 → UML / 时序图 / 组件图; 老牌 (2009-), 几乎所有 wiki / Confluence / IntelliJ / VS Code 都有插件. Trade-off: 语法老式 + 默认渲染丑, 但兼容性极强. [T02-S013] last_updated: 2026 active.

- **Mermaid** (Knut Sveidqvist). 何时用: Markdown 内嵌 (```mermaid 代码块), GitHub / GitLab / Notion 原生渲染; 是 README + ADR 内画图 *事实标准*. Trade-off vs PlantUML: Mermaid 渲染更现代 + 浏览器原生, 但表达能力略弱 (无完整 UML). 默认推荐. [T02-S014] [T02-S015] last_updated: 2026 active.

- **D2** (Terrastruct, 2022). 何时用: 现代声明式 diagram lang, 比 PlantUML 简洁, 输出 SVG/PNG 漂亮, 支持 Tala 自动布局. Trade-off: 较新, 生态不及 Mermaid/PlantUML. [T02-S016] last_updated: 2026 active.

- **IcePanel** (UK SaaS). 何时用: SaaS C4 协作工具, 支持团队多 view + git sync, 大企业 EA 场景. Trade-off: 商业付费 + 锁定. [T02-S017] last_updated: 2026 active.

- **adr-tools** (Nat Pryce, 基于 Michael Nygard 2011 原始博客). 何时用: bash CLI 在 `docs/adr/` 创建 numbered Markdown ADR (NNNN-decision-title.md), git-versioned. ADR 模板核心字段: Status / Context / Decision / Consequences. [T02-S018] [T02-S019] last_updated: 维护松散但格式仍是事实标准.

- **log4brains** (Thomvaill). 何时用: 把 docs/adr/*.md 渲染成 static site, 支持 search + history, 适合大型组织共享 ADR. Trade-off vs adr-viewer: log4brains 更现代 UI. [T02-S020] [T02-S021] last_updated: 2026 active.

## 2.3 API design + spec

- **OpenAPI 3.x** (OpenAPI Initiative, Linux Foundation). 何时用: REST API 标准 spec (YAML/JSON), code-gen 客户端 + mock + 文档; 3.1.0 (2021) 与 JSON Schema 兼容. Trade-off: design-first 还是 code-first 工程文化决定, 不背书单一. [T02-S022] [T02-S023] last_updated: OpenAPI 3.1.x 仍是当前版本.

- **Swagger Editor + Stoplight Studio** (SmartBear). 何时用: OpenAPI 可视化编辑 + lint + mock; Stoplight 偏 design-first 工作流, Swagger UI 偏 docs-as-spec. Trade-off: 都被 SmartBear 收购, 战略可能合并. [T02-S023] [T02-S024] last_updated: 2026 active.

- **Postman** (Postman Inc, San Francisco). 何时用: API 客户端 + collection + monitor + mock + 文档全家桶, 团队 SaaS 协作; 2024+ 增 AI 助手. Trade-off: SaaS 锁定 + 强制登录引发 backlash → Bruno + Hoppscotch 兴起. [T02-S025] last_updated: 2026 active.

- **Bruno** (Anoop Solar, 2023). 何时用: Postman 替代, 完全离线 + 文件存盘 (.bru 可入 git), 不强制账号. Trade-off: 协作功能弱于 Postman, 但工程师 git workflow 友好. [T02-S026] [T02-S027] last_updated: 2026 active.

- **Insomnia** (Kong). 何时用: REST + GraphQL + gRPC + WebSocket, 比 Postman 轻量. Trade-off: Kong 收购后定位有摇摆. [T02-S028] last_updated: 2026 active.

- **Hoppscotch** (Liyas Thomas). 何时用: 完全开源 web-based API 客户端, 可 self-host, 适合不想装客户端的快速测试. [T02-S029] last_updated: 2026 active.

- **GraphQL + Apollo Federation** (GraphQL Foundation; Apollo, 2015-). 何时用: 多服务聚合到单一图 (federation), 前端 over-fetch / under-fetch 痛点严重时. Trade-off: GraphQL 不是 REST 升级版, schema + N+1 + cache 复杂度高; 中小项目 REST + OpenAPI 更省心. [T02-S030] [T02-S031] last_updated: 2026 active.

- **Hasura / PostGraphile** (Hasura Inc; Graphile, OSS). 何时用: 把 PostgreSQL schema 自动暴露成 GraphQL/REST, 内部工具 + admin panel 速成. Trade-off: 业务逻辑不要写在 DB / GraphQL 层, 关键 path 仍需要 hand-written service. [T02-S032] [T02-S033] last_updated: 2026 active.

- **gRPC** (Google → CNCF). 何时用: 服务间二进制 RPC (HTTP/2 + protobuf), 强类型 + 多语言 codegen + streaming; 内部 east-west 流量首选. Trade-off: 浏览器不直接支持 (需 grpc-web), 防火墙 / 调试不如 HTTP/JSON 友好. [T02-S034] last_updated: 2026 active.

- **Buf** (Buf, Inc). 何时用: protobuf 工具链 (buf lint / buf breaking / buf gen / BSR registry), 替代手写 protoc + Makefile. Trade-off: 商业 SaaS 锁定的可能性. [T02-S035] last_updated: 2026 active.

- **AsyncAPI 3.x** (AsyncAPI Initiative, Linux Foundation). 何时用: OpenAPI 的事件 / 消息版本, Kafka / RabbitMQ / WebSocket / MQTT 等异步 channel 文档化. 与 OpenAPI 互补. [T02-S036] last_updated: AsyncAPI 3.0 (2023+).

## 2.4 Async messaging + streaming

- **Apache Kafka** (LinkedIn → Apache; Confluent). 何时用: 高吞吐 event log + 事件溯源 + CDC + streaming 数据中枢, 单集群 GB/s. Trade-off: ZooKeeper 运维历史负担 (KRaft mode 替代中), 中小项目用 SQS / RabbitMQ 更经济. [T02-S037] [T02-S038] last_updated: 2026 active (Kafka 3.x KRaft 已 GA).

- **Confluent Schema Registry + Connect** (Confluent). 何时用: Kafka 上的 Avro/Protobuf schema 演化管理 + 数据源 connector (JDBC/Debezium/Elasticsearch). Trade-off: 与 Confluent 商业捆绑深, OSS 替代 Apicurio. [T02-S039] last_updated: 2026 active.

- **Apache Pulsar** (Yahoo → Apache, StreamNative). 何时用: 计算与存储分离 (BookKeeper), 多租户 + geo-replication 原生, 大数据厂 + 多业务线场景. Trade-off vs Kafka: Pulsar 架构更现代但生态薄, 招聘难. [T02-S040] last_updated: 2026 active.

- **RabbitMQ** (Broadcom 收购). 何时用: 经典 AMQP broker, 任务队列 + RPC + 灵活 routing (exchange / queue / binding); 中小规模消息系统首选. Trade-off vs Kafka: RabbitMQ 不擅长事件溯源 + 高吞吐 log, Kafka 不擅长复杂 routing. [T02-S041] last_updated: 2026 active.

- **NATS** (Synadia → CNCF graduated). 何时用: 极轻量 pub-sub + request-reply + JetStream (持久化), 适合微服务通讯 + 边缘 IoT. Trade-off: 不是 Kafka 替代, 不擅长 long-term log. [T02-S042] last_updated: 2026 active.

- **Redpanda** (Redpanda Data, San Francisco). 何时用: Kafka API-compatible 的 C++ broker, 单进程无 JVM/ZK, 延迟更低; 想要 Kafka 但运维更简单时. Trade-off: 商业开源混合 license, 长期不确定. [T02-S043] last_updated: 2026 active.

- **AWS SQS+SNS / GCP Pub/Sub / Azure Service Bus** (cloud-managed). 何时用: 已在云内 + 不想自管 broker, SQS+SNS 经典 fan-out, Pub/Sub 全球 + at-least-once. Trade-off: 与云厂商深绑定, 多云迁移痛苦. [T02-S044] [T02-S045] [T02-S046] [T02-S047] last_updated: 2026 active.

- **Apache Flink** (Apache, Ververica/Alibaba). 何时用: 真正的 streaming 引擎 (低延迟 + exactly-once + 事件时间), 复杂 stateful streaming job. Trade-off vs Spark Streaming: Flink streaming-first, Spark batch-first. [T02-S048] last_updated: 2026 active.

- **Kafka Streams + ksqlDB** (Confluent). 何时用: 已在 Kafka 生态 + 不想引 Flink/Spark, Kafka Streams 嵌入 Java app, ksqlDB SQL-on-stream. Trade-off: 扩展性不如 Flink, 但运维简单. [T02-S049] [T02-S050] last_updated: 2026 active.

- **Materialize / RisingWave** (Materialize Inc; RisingWave Labs). 何时用: 物化视图风格 streaming database, SQL 持续维护 view; 实时 dashboard / 实时 join 场景. Trade-off: 新兴, 生态薄. [T02-S051] [T02-S052] last_updated: 2026 active.

- **Debezium** (Red Hat). 何时用: CDC (Change Data Capture) 从 PostgreSQL / MySQL / MongoDB / SQL Server binlog → Kafka, outbox pattern 标配. [T02-S053] last_updated: 2026 active.

- **Apache Beam** (Google → Apache). 何时用: 统一 batch + stream API, runner 可换 (Flink / Spark / Dataflow). Trade-off: 抽象层带性能与运维负担, 直接 Flink 常更简单. [T02-S054] last_updated: 2026 active.

## 2.5 Service mesh + API gateway

**重要 caveat** (Sam Newman + DHH + 多次 ThoughtWorks Radar Trial-not-Adopt): 微服务 < 30-50 个时 service mesh 几乎总是 over-engineering, sidecar 本身 CPU+内存+复杂度税常超过收益. "Often unnecessary" 是 2022-2026 行业 emerging consensus. 优先用 library (Resilience4j / Polly / Sentinel) + Envoy 单点 ingress 解决 70% 问题. [T02-S176]

- **Istio** (Google/IBM/Lyft → CNCF graduated). 何时用: 多语言微服务大规模 + 强制 mTLS + 细粒度 traffic policy; 1.29.x (2026) 通过 Ambient Mesh 移除 sidecar 减负. Trade-off: 历史 *复杂度怪兽*, 学习曲线陡, 中小团队不建议. [T02-S055] last_updated: Istio 1.29.x (2026).

- **Linkerd** (Buoyant → CNCF graduated). 何时用: 比 Istio 简单 10x, Rust 数据平面延迟低, 优先选项. Trade-off: 功能比 Istio 少 (e.g. 复杂流量切分), Buoyant 2024 起 stable 版本企业付费引发争议. [T02-S056] last_updated: 2026 active.

- **HashiCorp Consul Connect** (HashiCorp, BSL 2023+). 何时用: 已用 Consul 做服务发现 + 想要 mesh; 跨 K8s + VM + 多云一致. Trade-off: BSL license 引发社区分裂 → OpenBao 替代 Vault, mesh 替代不明显. [T02-S057] last_updated: 2026 active.

- **Cilium** (Isovalent → Cisco → CNCF). 何时用: eBPF 网络 + 安全 + observability + Cilium Service Mesh (无 sidecar), 现代 K8s 网络首选. Trade-off: 需较新 kernel. [T02-S058] last_updated: 2026 active.

- **Envoy + Gloo** (Lyft → CNCF; Solo.io). 何时用: Envoy 是 data plane 事实标准 (Istio / Cilium / AWS App Mesh 都用), Gloo 是 Solo.io 商业 control plane. [T02-S059] last_updated: 2026 active.

- **Kong / Tyk / Traefik / Apache APISIX** (API gateway). Kong (Kong Inc, Lua/Nginx 起家) 老牌生态强; Tyk Go-based 轻量; Traefik 自动 K8s discovery + Let's Encrypt 简单; APISIX (中国本土, Apache 顶级) etcd + 动态路由 + 高性能. Trade-off: 中国 + 大流量 → APISIX; K8s native + 简单 → Traefik; 企业 + 插件市场 → Kong. [T02-S060] [T02-S061] [T02-S062] [T02-S063] last_updated: 2026 active.

- **AWS API Gateway / Google Apigee** (managed). 何时用: serverless API + Lambda/Cloud Run 自然集成. Trade-off: cold start + 厂商锁定 + 调试比自托管痛. [T02-S064] [T02-S065] last_updated: 2026 active.

## 2.6 Orchestration + cloud runtime

**caveat** "K8s for everything 反模式": Kelsey Hightower (K8s 早期布道者) 多次公开 "If you can ship without K8s, ship without K8s." 100 个 node 以下 + 50 个服务以下, K8s 运维税常 > 收益. Render / Fly.io / ECS / Cloud Run 通常更经济. [T02-S066] [T02-S177]

- **Kubernetes** (CNCF graduated, Google origin). 1.36.1 released 2026-05-13. 何时用: 50+ 服务规模 + 多团队多租户 + 需 portable infra. Trade-off: 复杂度 + 招聘成本 + YAML 山, 不是默认起点. [T02-S066] [T02-S067] last_updated: K8s 1.36.1 (2026-05-13).

- **Nomad** (HashiCorp). 何时用: 比 K8s 简单 5x, 支持容器 + VM + raw binary, 与 Consul + Vault 整合; Cloudflare / Roblox 大规模用. Trade-off: 生态比 K8s 薄, BSL license 2023+. [T02-S068] last_updated: 2026 active.

- **AWS ECS+Fargate / Cloud Run / Azure Container Apps** (managed). 何时用: 不想运维 K8s + 已在云内, ECS 经典, Cloud Run scale-to-zero, Container Apps 兼有. Trade-off: 锁定 + 多云迁移痛. [T02-S069] [T02-S070] [T02-S071] last_updated: 2026 active.

- **Fly.io machines / Render / Railway** (PaaS, 2020+). 何时用: < 10 服务的初创团队, 一行 `fly deploy` / `git push`, 自带 anycast + Postgres + 全球部署; DHH 推荐区间. Trade-off: 大规模性价比反转, vendor 财务稳定性需关注. [T02-S072] [T02-S073] [T02-S074] last_updated: 2026 active.

- **Helm / Kustomize** (K8s package + overlay). Helm 是 K8s 应用打包事实标准 (chart 模板), Kustomize 是 overlay 风格 patch (无模板). Trade-off: 复杂应用 Helm, 多环境 patch Kustomize, 常组合用. [T02-S075] [T02-S076] last_updated: 2026 active.

- **Crossplane** (Upbound → CNCF). 何时用: 用 K8s CRD 管理云资源 (AWS RDS / GCP Bucket 等), 把 Terraform 思路搬到 control plane. Trade-off: 较新, 团队需 K8s 深度. [T02-S077] last_updated: 2026 active.

## 2.7 Database 10 子类 (OLTP / 文档 / 图 / KV / 搜索 / OLAP / HTAP / 时序)

**关键决策树** (节末 2.X 详写). 简要原则: 90% 的应用从 **PostgreSQL** 起步是正确答案 (DHH / Kleppmann 共识); 文档 / KV / search 都可后加.

### OLTP (relational)
- **PostgreSQL** 18.4 (2026-05-14). 行业默认: JSON / 全文 / 地理 / 扩展生态 (pgvector / Timescale / Citus) 无敌. [T02-S078]
- **MySQL** (Oracle). 阿里 / 字节 / 大型 web 仍主流; InnoDB + binlog 成熟. [T02-S079]
- **MariaDB** (MySQL 创始人 fork). 政府 + 中欧偏好, 与 MySQL 不再完全兼容. [T02-S080]
- **SQLite** (Hipp). 嵌入式 + edge + CLI 工具; rqlite / litestream 让它进生产; Rails 8 / Fly.io 推动复兴. [T02-S081]
- **CockroachDB / TiDB / YugabyteDB / Spanner / Aurora / Vitess** (Distributed SQL / NewSQL). CockroachDB Google Spanner 思路开源; TiDB (PingCAP, 杭州) 中国本土 HTAP 顶尖; Yugabyte PG-compatible; Spanner Google managed; Aurora AWS managed MySQL/PG; Vitess MySQL 水平分片 (YouTube). [T02-S082] [T02-S083] [T02-S084] [T02-S085] [T02-S086] [T02-S087] last_updated: 2026 active.

### 文档
- **MongoDB** (MongoDB Inc). 文档 DB 事实标准, 4.0+ 多文档事务. Trade-off: 80% 用例 PostgreSQL JSONB 就够. [T02-S088]
- **DynamoDB / Cassandra / ScyllaDB / Couchbase**. DynamoDB AWS managed KV+wide-column; Cassandra 多数据中心写无敌; ScyllaDB C++ Cassandra-compatible 性能 10x; Couchbase 文档+KV+查询. [T02-S089] [T02-S090] [T02-S091] [T02-S093]

### KV / 缓存
- **Redis** 7.x. 缓存 / 锁 / 队列 / pub-sub / streams 全能; 2024 license 改 SSPL → Valkey (Linux Foundation fork) 兴起. [T02-S092]

### 图
- **Neo4j / DGraph**. Neo4j Cypher 是事实标准查询语言; DGraph GraphQL-native. Trade-off: 大多数 "图" 需求 PostgreSQL recursive CTE 就够, 真图 DB 是社交 / 反欺诈 / 知识图谱. [T02-S094] [T02-S095]

### 搜索
- **Elasticsearch / OpenSearch / Meilisearch / Typesense**. ES 老牌 + 强 (license 改 SSPL 引发 AWS fork → OpenSearch); Meilisearch / Typesense 现代轻量适合产品内 search bar. [T02-S096] [T02-S097] [T02-S098] [T02-S099]

### OLAP
- **ClickHouse / DuckDB / StarRocks / Apache Doris / Snowflake / BigQuery / Redshift / Databricks / Apache Druid / Apache Pinot**. ClickHouse (Yandex 起源) 列式分析事实标准, DuckDB 嵌入式 OLAP (analytics laptop), StarRocks / Apache Doris (中国 OLAP 双雄), Snowflake / BigQuery / Redshift 云仓三巨头, Databricks lakehouse, Druid / Pinot 实时 OLAP. [T02-S100]-[T02-S109]

## 2.8 Observability + continuous profiling

- **OpenTelemetry (OTel)** (CNCF, OpenTracing+OpenCensus 合并). 何时用: 厂商中立 metric/log/trace SDK + collector, *2024+ 任何新项目 instrument 起点*. Trade-off: SDK 各语言成熟度不一, log signal 较 trace/metric 晚 GA. [T02-S110] last_updated: 2026 active (OTel log GA).

- **Jaeger / Zipkin** (CNCF graduated; Twitter 起源). 分布式 trace 后端, Jaeger Uber 起源更现代. [T02-S111] [T02-S112]

- **Prometheus + Grafana + Loki** (CNCF; Grafana Labs). 开源 metric+dashboard+log 黄金组合; Prometheus pull-based + PromQL 事实标准. Trade-off: 长期存储要外挂 (Thanos / Mimir / Cortex). [T02-S113] [T02-S114] [T02-S115]

- **Honeycomb** (Charity Majors). 何时用: 高 cardinality event 风格 observability (BubbleUp 异常归因), 调试微服务长尾延迟无敌. Trade-off: 思维方式从 dashboard → query, 团队要 retrain. [T02-S116]

- **Datadog** (NYC, 上市). 大企业 all-in-one (APM + log + RUM + security), 极贵但确实省事. Trade-off: 账单 surprise 是行业 meme, 2024+ 引发 cost optimization 浪潮. [T02-S117]

- **New Relic / Splunk / Dynatrace** (legacy enterprise). 大企业既有合同栈, Splunk 强 log + SIEM. [T02-S118] [T02-S119] [T02-S120]

- **Sentry** (Sentry Inc, OSS). 错误追踪事实标准, 前端 + 后端 + 移动端通吃. [T02-S121]

- **Apache SkyWalking** (吴晟, OpenInception 创始人, Apache 顶级). 何时用: 国产 APM 首选, 中国大厂 + 信创合规场景; 多语言 agent + topology 自动发现 + log+trace+metric 统一. Trade-off: 国际生态薄于 Datadog, 但国内文档与社区强. [T02-S122] last_updated: 2026 active.

- **Continuous profiling**: Grafana Pyroscope / Polar Signals / Parca (OSS, eBPF) / pprof (Go) / async-profiler (JVM). 何时用: 2024+ 性能优化必备, "看 CPU/内存 flame graph 而不是猜". [T02-S123] [T02-S124] [T02-S125] [T02-S126]

## 2.9 Reliability + chaos + load test + feature flag

- **Chaos Engineering**: **Chaos Monkey** (Netflix, 始祖, 现已被 Simian Army 替代) / **Chaos Mesh** (CNCF, PingCAP 起源, K8s-native) / **LitmusChaos** (CNCF) / **Gremlin** (SaaS) / **AWS FIS** (managed). 何时用: 已有冗余 + 已 SLO 化的成熟系统; 不成熟系统做 chaos 是 chaos. [T02-S127] [T02-S128] [T02-S129] [T02-S130] [T02-S131]

- **Load test**: **k6** (Grafana, Go runtime + JS DSL, 现代首选) / **Locust** (Python, 写测试爽) / **Artillery** (Node) / **Apache JMeter** (Java 经典 GUI) / **Gatling** (Scala 高性能) / **Vegeta** (Go CLI 极简). 默认: 现代项目 k6, Python 团队 Locust, 传统企业 JMeter. [T02-S132]-[T02-S137]

- **Feature flag + experimentation**: **LaunchDarkly** (市场领导, 贵) / **Statsig** (Meta 起源, 实验强) / **GrowthBook** (OSS, self-host) / **Unleash** (OSS, 欧洲) / **Optimizely** (web exp 老牌). Trade-off: 自己造 feature flag 是反模式, 但 SaaS 价格也常打脸 → GrowthBook / Unleash. [T02-S138] [T02-S139] [T02-S140] [T02-S141]

## 2.10 Architecture testing + AI 辅助 + 文档

- **Architecture testing** (把"架构规则"写成测试断言, 防腐烂): **ArchUnit** (Java/JVM, 事实标准) / **NetArchTest** (.NET) / **Konsist** (Kotlin) / **pyArchTest** (Python). 何时用: 团队 > 10 人 + 已有 layered/hexagonal 架构想防新人破坏. [T02-S142] [T02-S143] [T02-S144]

- **OpenRewrite** (Moderne, Spring Lab 起源). 何时用: 大规模自动 refactor (Java 8→17 / Spring Boot 2→3 / log4j CVE 修复), recipe 可写. Trade-off: 学 recipe DSL 有门槛. [T02-S145]

- **Semgrep** (r2c). 何时用: 模式式静态分析, 自定义规则 (e.g. "禁止 controller 直接访问 repository"), 比正则强比 AST tool 简单. [T02-S146]

- **AI 辅助** (2024-2026 currently hot, **must caveat**): **GitHub Copilot** (Microsoft, IDE-native 主流) / **Cursor** (AI-native IDE, 2024+ 现象级) / **Claude Code** (Anthropic CLI agent) / **Aider** (OSS CLI, git-aware) / **Codeium/Windsurf** (免费 tier 强). 何时用: code generation / 测试生成 / boilerplate / 文档翻译 — 是 productivity boost. **反例 caveat**: ❌ 不靠 LLM 决定 *service boundary / polyglot persistence 选型 / consistency 模型选择* 等关键架构 trade-off; 这些需要业务语境 + 长期演化判断, LLM 给的常是 "训练集中位数" 答案, 对 founder/staff+ 架构师没有信号价值. 用 LLM 做 "rubber duck + spec drafting + 实现加速", 不做 decision-maker. [T02-S147] [T02-S148] [T02-S149] [T02-S150] [T02-S151] last_updated: 2026 active hype 期.

- **Backstage** (Spotify → CNCF). 开发者门户事实标准, 服务目录 + 文档 + scaffolding + plugin 生态. Trade-off: 自建 + 维护成本高, 中小公司不建议. [T02-S152]

- **Docusaurus / MkDocs Material** (Meta; Martin Donath). 工程文档 + ADR 静态站点; Docusaurus React 生态强, MkDocs Material 配置极简. [T02-S153] [T02-S154]

- **IaC**: **Terraform / OpenTofu / Pulumi / AWS CDK**. Terraform HashiCorp 2023 改 BSL → OpenTofu fork (Linux Foundation), 多数 OSS-first 团队迁到 OpenTofu; Pulumi 真实编程语言 (TS/Go/Python); AWS CDK Amazon-only 但 ergonomic. [T02-S155] [T02-S156] [T02-S157] [T02-S158]

## 2.11 中国本土补充

**为何独立成节**: 中国大厂规模 (春晚 / 双 11 / 微信红包) 对架构压力远超国际 SaaS, 阿里 / 腾讯 / 蚂蚁 / 京东 / 字节 / 美团 把内部解 OSS, 多数已 Apache 顶级毕业 (Dubbo / RocketMQ / SkyWalking / APISIX / Doris / ShardingSphere). 这是 *中国规模本土实践*, 国外团队也在用 (e.g. 美国 / 欧洲 SkyWalking + APISIX 用户增长).

- **Apache Dubbo** (阿里梁飞 2008 → Apache, 当前 3.3.6 / 2024-10). Java RPC 框架 + 服务治理, 国内 Spring Cloud 的对手; 3.x 支持 Triple (gRPC over HTTP/2) + Reactive. [T02-S159] [T02-S160] last_updated: 3.3.6 (2024-10).

- **Apache RocketMQ** (阿里 2012 → Apache, 5.5.0 / 2025-04). 阿里淘宝双 11 trillion-message 主力, 5.x 引入 Lite Mode (AI 场景), 强事务消息支持. Trade-off vs Kafka: RocketMQ 在中国生态强, Kafka 国际生态强. [T02-S161] [T02-S162] last_updated: 5.5.0 (2025-04).

- **Apache SkyWalking** (吴晟 2015 → Apache, OpenInception 主席). 国产 APM 第一, 多语言 agent + topology, 国内信创合规事实标准. [T02-S122] last_updated: 2026 active.

- **Apache APISIX** (支流科技 / API7, 王院生). 高性能 API gateway, etcd + 动态路由 + 插件式, 2020 Apache 顶级; 单实例 18000 QPS, 性能超 Kong. [T02-S062] last_updated: 2026 active.

- **Apache ShardingSphere** (京东 张亮). 数据库 sharding / 分库分表中间件, 透明化 (JDBC 代理或 Proxy 两种模式). [T02-S163] last_updated: 2026 active.

- **Nacos** (阿里). 服务注册发现 + 动态配置 一站式, Spring Cloud Alibaba 默认搭档, Dubbo 也用. [T02-S164] last_updated: 2026 active.

- **Sentinel** (阿里, Eric Zhao). 流量控制 + 熔断 + 降级 + 系统自适应保护; 双 11 流量入口本机限流 历史验证. [T02-S165] last_updated: 2026 active.

- **Apache Seata** (阿里 → Apache, 2024 顶级). 分布式事务 (AT/TCC/SAGA/XA), 国内微服务事务事实标准. [T02-S166] last_updated: 2026 active.

- **TDengine** (涛思, 陶建辉). 国产时序数据库, 物联网 / 工业数据 场景, 集群版开源 (3.x). 与 InfluxDB / TimescaleDB 直接竞争. [T02-S167] last_updated: 2026 active.

- **蚂蚁 SOFAStack** (蚂蚁集团). 包含 **SOFABoot** (Spring Boot 扩展) + **SOFARPC** (RPC) + **MOSN** (Go service mesh data plane, Envoy 替代) + **SOFAJRaft** (Raft) + **SOFARegistry**. 金融场景事实标准 (蚂蚁付宝). [T02-S168] [T02-S169] [T02-S170] last_updated: 2026 active.

- **腾讯 TARS** (腾讯 → Linux Foundation TARS Foundation). 微信内部多语言 RPC 框架 (C++/Java/Go/Node/PHP), 包名 + 模板 + 自动 codegen. Trade-off: 出腾讯系生态薄. [T02-S171] last_updated: 2026 active.

- **OceanBase** (蚂蚁集团, 阳振坤). 国产 NewSQL HTAP, 双 11 / 工行 / 建行 已替 Oracle; 2023 OSS (Apache 2.0); MySQL 兼容. *国产化替代浪潮* 政府金融首选. [T02-S172] [T02-S173] last_updated: 2026 active.

## 2.X 工具选型决策树 (4 个常见场景)

### 场景 1: "新 web app, 服务 < 10 个, 团队 5 人, 想快速上线"

**推荐栈** (DHH / Stack Overflow / Shopify case 共识):
- 后端: **modular monolith** (Rails / Django / Spring Boot / .NET / NestJS), 不切微服务
- DB: **PostgreSQL** (单一 DB 兼 JSON+全文+地理), 加 **Redis** 做 cache+queue
- 部署: **Fly.io / Render / Railway** (一行 git push), 不上 K8s
- 文档+图: **Mermaid in README** + **adr-tools 文件 ADR**
- API: **OpenAPI + Postman/Bruno**, 不上 GraphQL
- Observability: **Sentry** (errors) + **Grafana Cloud free tier** 或 **Honeycomb free tier**, 不上 Datadog
- Feature flag: **GrowthBook self-host** 或 写一张 DB 表
- CI: **GitHub Actions**, 不上 Argo Workflow

**反例**: 这个规模上 K8s + Istio + Kafka + Cassandra + multi-DB 是工程自爽, 不会让产品更快上线. 参考 Stack Overflow 9 服务器规模 [T02-S179] / Shopify 长期 modular monolith [T02-S178] / DHH "we left the cloud" [T02-S177].

### 场景 2: "已有 100+ 微服务, 中大厂规模, 多团队多语言"

**推荐栈**:
- 编排: **Kubernetes** + **Helm** + (可选) **Crossplane / Argo CD**
- Service mesh: **Linkerd 优先** (复杂度低 + Rust data plane), Istio 仅当真需要细粒度 traffic policy; *默认怀疑你需要 mesh* [T02-S176]
- API gateway: **Envoy** 或 **APISIX** ingress
- Messaging: **Kafka + Schema Registry + Debezium** (CDC) — 一个事件中枢比 N 个点对点 RPC 健康
- DB: **polyglot persistence** — OLTP PostgreSQL + cache Redis + 搜索 Elasticsearch/OpenSearch + 分析 ClickHouse + 文档/时序按需; 限制 DB 种类 ≤ 5
- Observability: **OpenTelemetry SDK 强制** + 后端 Grafana stack 自托管 *或* Datadog/Honeycomb 托管 (二选一别混)
- Dev portal: **Backstage** + Service catalog 强制
- Architecture testing: **ArchUnit** + CI 阻塞 boundary 违规
- IaC: **OpenTofu / Pulumi**, 不允许手工点云控制台

### 场景 3: "中国本土合规高并发, 春晚 / 双 11 / 国资 / 信创"

**推荐栈**:
- 服务治理: **Dubbo 3.x** (Java) + **Nacos** (注册中心 + 配置) + **Sentinel** (限流熔断) + **Seata** (分布式事务)
- Messaging: **RocketMQ 5.x** (事务消息 + 万亿级 / 双 11 验证); 海外业务用 Kafka
- API gateway: **Apache APISIX** (国产 + 高性能 + 信创)
- Observability: **Apache SkyWalking** (国产 APM, 信创合规)
- Sharding: **ShardingSphere** (透明分库分表)
- DB: 金融核心 **OceanBase** 替 Oracle; 互联网业务 **TiDB** (HTAP); 时序 **TDengine**
- 金融场景特殊: **蚂蚁 SOFAStack** 全家桶 (SOFABoot + SOFARPC + MOSN service mesh + SOFAJRaft)
- 腾讯系: **TARS** (C++/多语言 RPC)
- *国产化替代*: GaussDB / OpenGauss (华为) / TDSQL (腾讯) 等政策驱动

参见 [T02-S159]-[T02-S173].

### 场景 4: "front-end + back-end 数据流, 全栈现代 web/mobile"

**推荐栈**:
- 大型团队 + 多客户端: **GraphQL + Apollo Federation** (一图聚合多服务, 客户端按需 query)
- 中小型: **REST + OpenAPI 3.x** (code-gen 客户端 + 文档), Bruno/Postman 测试
- TypeScript 单 repo (全栈): **tRPC** (类型直通, 无 spec 中间层) 或 **GraphQL + GraphQL Codegen**
- 内部 east-west 流量: **gRPC + Buf** (强类型 + streaming)
- 事件 / 推送: **WebSocket** 或 **SSE** + **AsyncAPI** spec; 高规模 **Centrifugo / Ably / Pusher**
- 状态管理 (客户端):
  - **server state**: **TanStack Query (React Query)** 或 **SWR** — *2024+ 默认*
  - **client state (小)**: **Zustand / Jotai** (轻量) — 默认起点
  - **client state (大企业)**: **Redux Toolkit + RTK Query** (复杂状态机)
- 表单: **React Hook Form + Zod schema**
- Auth: **Clerk / Auth0 / Supabase Auth** (托管) 或 **Lucia / NextAuth** (自托管)
- 边缘: **Cloudflare Workers / Vercel Edge / Deno Deploy** (低延迟 + 全球分发)

---

> Track 02 done. 180 sources. ~150+ 工具 (国际 ~140 / 中国本土 ≥ 11). 10 大类 ✓ + 决策树 4 场景 ✓.
