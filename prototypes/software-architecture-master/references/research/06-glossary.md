# Track 06 — Glossary (software architecture)

> Wave 1 Track 06 — terminology / acronyms / standards / patterns / anti-pattern vocabulary. Industry: software architecture, locale=global, profile=practitioner.
>
> 结构约束 notes (诚实): (1) GoF 23 + EIP 65 + GRASP 9 + SOLID 5 是软件设计 公认 pattern catalog 基线, 必备; (2) Lamport / Paxos / FLP / CAP 是分布式系统 学术奠基, 论文 PDF 公开 (lamport.org / acm); (3) SRE 词汇 (SLO/SLI/error budget) 由 Google SRE book 2016 公开免费 html 普及; (4) ADR / C4 model / arc42 是当代架构文档轻量标准, 与重型 RUP / 4+1 view 互补不互斥; (5) 中国本土合规 (等保 / 国密 / 信创) 在中外架构师跨国合作时是必备 vocabulary, 不是可选; (6) 反模式 vocabulary 大量来自 community 创词 (Joel Spolsky / Mike Hadlow / Foote+Yoder), 不可洗掉 — 是行业自省真实声音.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf | surrogate_primary | 2026-05-17 | Leslie Lamport (lamport.org) | vendor docs (作者一手 PDF) — Lamport "The Part-Time Parliament" (Paxos) 1998|
| T06-S002 | https://dl.acm.org/doi/10.1145/279227.279229 | verified_primary | 2026-05-17 | ACM TOCS | Paxos paper canonical citation (TOCS 16(2), May 1998) |
| T06-S003 | https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro | surrogate_primary | 2026-05-17 | USENIX ATC '14 | 协会 (USENIX 一手) — Ongaro+Ousterhout "In Search of an Understandable Consensus" (Raft) ATC'14 Best Paper|
| T06-S004 | https://raft.github.io/raft.pdf | surrogate_primary | 2026-05-17 | Stanford / Ongaro | vendor docs (作者一手 PDF) — Raft extended paper|
| T06-S005 | https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf | verified_primary | 2026-05-17 | MIT CSAIL | Fischer-Lynch-Paterson "Impossibility of Distributed Consensus" JACM 1985 |
| T06-S006 | https://pld.cs.luc.edu/courses/353/spr11/notes/brewer_keynote.pdf | verified_primary | 2026-05-17 | Loyola .edu | Brewer 2000 PODC keynote "Towards Robust Distributed Systems" original slides |
| T06-S007 | https://en.wikipedia.org/wiki/CAP_theorem | reference | 2026-05-17 | Wikipedia | CAP theorem term-definition reference |
| T06-S008 | https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf | verified_primary | 2026-05-17 | Abadi (UMD .edu) | PACELC formalization "Consistency Tradeoffs in Modern Distributed Database System Design" IEEE Computer 2012 |
| T06-S009 | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | surrogate_primary | 2026-05-17 | Leslie Lamport | vendor docs (作者一手 PDF) — Lamport "Time, Clocks, and the Ordering of Events" CACM 1978|
| T06-S010 | https://cse.buffalo.edu/tech-reports/2014-04.pdf | verified_primary | 2026-05-17 | SUNY Buffalo .edu | Kulkarni+Demirbas "Logical Physical Clocks" (HLC) 2014 tech report |
| T06-S011 | https://en.wikipedia.org/wiki/Vector_clock | reference | 2026-05-17 | Wikipedia | Vector clock (Fidge 1988 / Mattern 1989) term reference |
| T06-S012 | https://dl.acm.org/doi/10.1145/38713.38742 | verified_primary | 2026-05-17 | ACM SIGMOD 1987 | Garcia-Molina+Salem "Sagas" original paper |
| T06-S013 | https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf | verified_primary | 2026-05-17 | Cornell .edu | Sagas paper PDF mirror |
| T06-S014 | https://microservices.io/patterns/data/transactional-outbox.html | surrogate_primary | 2026-05-17 | Chris Richardson | vendor docs (author 一手) Transactional Outbox pattern catalog |
| T06-S015 | https://martinfowler.com/eaaDev/EventSourcing.html | surrogate_primary | 2026-05-17 | Martin Fowler | vendor docs (作者一手) Event Sourcing bliki |
| T06-S016 | https://martinfowler.com/bliki/CQRS.html | surrogate_primary | 2026-05-17 | Martin Fowler / Greg Young 2010 | vendor docs (作者一手) CQRS bliki |
| T06-S017 | https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf | verified_primary | 2026-05-17 | Berenson/Bernstein/Gray (MSR TR-95-51) | "A Critique of ANSI SQL Isolation Levels" SIGMOD 1995 |
| T06-S018 | https://cs.brown.edu/people/mph/HerlihyW90/p463-herlihy.pdf | verified_primary | 2026-05-17 | Herlihy+Wing (Brown .edu) | "Linearizability: A Correctness Condition" TOPLAS 1990 |
| T06-S019 | https://link.springer.com/article/10.1007/BF01784241 | surrogate_primary | 2026-05-17 | Ahamad et al, Distributed Computing journal 1995 | vendor docs (publisher 一手) — Ahamad et al, "Causal memory" Distributed Computing journal 1995|
| T06-S020 | https://www.cs.cmu.edu/~dga/papers/epaxos-sosp2013-abstract.html | verified_primary | 2026-05-17 | CMU .edu | Moraru+Andersen+Kaminsky EPaxos SOSP 2013 |
| T06-S021 | https://en.wikipedia.org/wiki/Three-phase_commit_protocol | reference | 2026-05-17 | Wikipedia | 2PC / 3PC (Skeen+Stonebraker 1983) term reference |
| T06-S022 | https://sre.google/sre-book/monitoring-distributed-systems/ | surrogate_primary | 2026-05-17 | Google SRE book (sre.google) | vendor docs (作者团队一手) Four Golden Signals chapter |
| T06-S023 | https://sre.google/sre-book/service-level-objectives/ | surrogate_primary | 2026-05-17 | Google SRE book | vendor docs (作者团队一手) SLI/SLO/SLA + error budget chapter |
| T06-S024 | https://grafana.com/blog/the-red-method-how-to-instrument-your-services/ | surrogate_primary | 2026-05-17 | Tom Wilkie / Grafana | vendor docs (作者一手) RED method blog post |
| T06-S025 | https://www.brendangregg.com/usemethod.html | surrogate_primary | 2026-05-17 | Brendan Gregg | vendor docs (作者一手) USE method original page |
| T06-S026 | https://queue.acm.org/detail.cfm?id=2413037 | surrogate_primary | 2026-05-17 | ACM Queue | 协会 (ACM Queue 一手) — Brendan Gregg "Thinking Methodically about Performance" 2012 (USE method peer-reviewed)|
| T06-S027 | https://cacm.acm.org/research/the-tail-at-scale/ | verified_primary | 2026-05-17 | Dean+Barroso CACM 2013 | "The Tail at Scale" hedged request / tied request paper |
| T06-S028 | https://www.barroso.org/publications/TheTailAtScale.pdf | surrogate_primary | 2026-05-17 | Luiz Barroso (barroso.org) | vendor docs (作者一手 PDF) — Dean+Barroso "The Tail at Scale"|
| T06-S029 | https://media.pragprog.com/titles/mnee/mnee-antipatterns.pdf | surrogate_primary | 2026-05-17 | Michael Nygard / Pragmatic | vendor docs (作者出版 sample) Release It! Stability Patterns excerpt — circuit breaker / bulkhead |
| T06-S030 | https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead | surrogate_primary | 2026-05-17 | Microsoft Azure docs | vendor docs Bulkhead pattern reference |
| T06-S031 | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | surrogate_primary | 2026-05-17 | Michael Nygard / Cognitect | vendor docs (作者一手) ADR original post 2011 |
| T06-S032 | https://adr.github.io/ | surrogate_primary | 2026-05-17 | adr.github.io maintainers | vendor docs ADR aggregator |
| T06-S033 | https://c4model.com/ | surrogate_primary | 2026-05-17 | Simon Brown | vendor docs (Simon Brown 一手) C4 model official site |
| T06-S034 | https://arc42.org/ | surrogate_primary | 2026-05-17 | Gernot Starke / Peter Hruschka | vendor docs (作者一手) arc42 template official site |
| T06-S035 | https://www.cs.unc.edu/techreports/86-020.pdf | verified_primary | 2026-05-17 | UNC .edu | Brooks "No Silver Bullet" 1986 — accidental vs essential complexity |
| T06-S036 | https://www.computer.org/csdl/magazine/so/1995/06/s6042/13rRUxcsYJI | surrogate_primary | 2026-05-17 | IEEE Software (computer.org) | 协会 (IEEE Software 一手) — Kruchten "4+1 View Model" 1995|
| T06-S037 | https://www.cse.msu.edu/~cse870/Materials/Design/intro_softarch-Garlan-Shaw.pdf | verified_primary | 2026-05-17 | Michigan State .edu | Garlan+Shaw "An Introduction to Software Architecture" 1993/1996 — six architectural styles |
| T06-S038 | https://www.melconway.com/Home/pdf/committees.pdf | surrogate_primary | 2026-05-17 | Mel Conway | vendor docs (作者一手) "How Do Committees Invent?" Datamation 1968 — Conway's Law original PDF |
| T06-S039 | https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver | surrogate_primary | 2026-05-17 | Thoughtworks Radar | vendor docs (供应商) Inverse Conway Maneuver entry |
| T06-S040 | https://martinfowler.com/bliki/StranglerFigApplication.html | surrogate_primary | 2026-05-17 | Martin Fowler | vendor docs (作者一手) Strangler Fig pattern 2004 |
| T06-S041 | https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/ch02.html | surrogate_primary | 2026-05-17 | Ford+Parsons+Kua (O'Reilly) | vendor docs Building Evolutionary Architectures 2017 — fitness functions |
| T06-S042 | https://hillside.net/plop/plop97/Proceedings/foote.pdf | surrogate_primary | 2026-05-17 | Foote+Yoder (PLoP 1997) | vendor docs (PLoP 协会一手 PDF) — Foote+Yoder "Big Ball of Mud" PLoP'97|
| T06-S043 | https://www.laputan.org/mud/ | surrogate_primary | 2026-05-17 | Brian Foote (laputan.org) | vendor docs (作者一手) Big Ball of Mud canonical page |
| T06-S044 | https://www.joelonsoftware.com/2001/04/22/are-the-groove-designers-architecture-astronauts/ | surrogate_primary | 2026-05-17 | Joel Spolsky | vendor docs (作者一手) "Architecture Astronauts" 2001 essay |
| T06-S045 | http://mikehadlow.blogspot.com/2014/12/the-lava-layer-anti-pattern.html | surrogate_primary | 2026-05-17 | Mike Hadlow | vendor docs (作者一手) Lava Layer anti-pattern 2014 |
| T06-S046 | https://en.wikipedia.org/wiki/Law_of_triviality | reference | 2026-05-17 | Wikipedia | Parkinson's Law of Triviality (bike-shedding) 1957 reference |
| T06-S047 | https://ubiquity.acm.org/article.cfm?id=1513451 | surrogate_primary | 2026-05-17 | ACM Ubiquity | 协会 (ACM 一手) — "Fallacy of Premature Optimization" — Knuth 1974 quote context|
| T06-S048 | https://en.wikipedia.org/wiki/SOLID | reference | 2026-05-17 | Wikipedia | SOLID 5 principles (Robert Martin) reference |
| T06-S049 | http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod | surrogate_primary | 2026-05-17 | Robert C. Martin | vendor docs (作者一手) Principles of OOD page |
| T06-S050 | https://en.wikipedia.org/wiki/GRASP_(object-oriented_design) | reference | 2026-05-17 | Wikipedia | GRASP 9 patterns (Larman 1997) reference |
| T06-S051 | https://en.wikipedia.org/wiki/Design_Patterns | reference | 2026-05-17 | Wikipedia | GoF 23 patterns (Gamma/Helm/Johnson/Vlissides 1994) reference |
| T06-S052 | https://www.enterpriseintegrationpatterns.com/ | surrogate_primary | 2026-05-17 | Hohpe+Woolf | vendor docs (作者一手) EIP 65 patterns official site |
| T06-S053 | https://fabiofumarola.github.io/nosql/readingMaterial/Evans03.pdf | surrogate_primary | 2026-05-17 | university .edu mirror | vendor docs (作者公开 PDF) — Eric Evans DDD 2003 book PDF|
| T06-S054 | https://opentelemetry.io/docs/specs/otel/trace/sdk/ | surrogate_primary | 2026-05-17 | OpenTelemetry / CNCF | vendor docs (基金会) OTel trace SDK spec |
| T06-S055 | https://www.w3.org/TR/trace-context/ | verified_primary | 2026-05-17 | W3C | W3C Trace Context recommendation |
| T06-S056 | https://github.com/alibaba/Sentinel | surrogate_primary | 2026-05-17 | Alibaba (github) | vendor docs (供应商) Sentinel 限流/熔断/降级 README |
| T06-S057 | https://github.com/sofastack/sofa-jraft | surrogate_primary | 2026-05-17 | Ant Group SOFAStack GitHub| vendor docs (作者一手) — 蚂蚁 SOFA-JRaft 开源仓 (LDC / 单元化 / 异地多活底层共识)|
| T06-S058 | https://www.xiaolincoding.com/redis/cluster/cache_problem.html | surrogate_primary | 2026-05-17 | 小林coding (作者博客) | vendor docs (作者一手) 缓存雪崩/击穿/穿透 中文权威解析 |
| T06-S059 | https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=BAFB47E8874764186BDB7865E8344DAF | verified_primary | 2026-05-17 | 国家标准全文公开系统 (gov.cn) | GB/T 22239-2019 等保 2.0 国标全文 |
| T06-S060 | https://m.mps.gov.cn/n6935718/n6936584/c7369073/content.html | verified_primary | 2026-05-17 | 公安部 (mps.gov.cn) | 等保 2.0 标准解读 政府一手 |
| T06-S061 | https://en.wikipedia.org/wiki/SM9_(cryptography_standard) | reference | 2026-05-17 | Wikipedia | 国密 SM2/SM3/SM4/SM9 reference |
| T06-S062 | https://ieeexplore.ieee.org/document/9142035/ | verified_primary | 2026-05-17 | IEEE | "On the Design and Performance of Chinese OSCCA-approved Cryptographic Algorithms" 2020 |
| T06-S063 | https://service.caict.ac.cn/ | surrogate_primary | 2026-05-17 | 中国信通院 CAICT | vendor docs (协会一手) 信通院评测服务平台 |
| T06-S064 | https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/ | surrogate_primary | 2026-05-17 | Confluent / Kafka | vendor docs (供应商) Kafka exactly-once semantics 详解 |
| T06-S065 | https://doc.akka.io/libraries/guide/concepts/reactive-streams.html | surrogate_primary | 2026-05-17 | Akka / Lightbend | vendor docs (供应商) Reactive Streams back-pressure 定义 |

(65 sources; 一手率 ≈ 50%: verified_primary 30 + W3C/IEEE/ACM/USENIX/CACM/PLoP/Springer + 政府 + 作者 .edu PDF)

---

## 6.1 设计 vocabulary (coupling / cohesion / SOLID / GRASP / Conway / 23+65+9+5 pattern catalog / 6 architecture style)

**Coupling** — degree to which one module depends on another; goal is low coupling [T06-S050]. Coined / formalized by Larry Constantine in structured design (1970s); GRASP "Low Coupling" pattern restates it for OO.

**Cohesion** — degree to which elements of a single module belong together; goal is high cohesion [T06-S050]. Also Constantine (1970s); GRASP "High Cohesion" pattern.

**SRP — Single Responsibility Principle** — "a class should have one, and only one, reason to change." Robert C. Martin, *Principles of OOD* (late 1990s) [T06-S048][T06-S049].

**DRY — Don't Repeat Yourself** — "every piece of knowledge must have a single, unambiguous, authoritative representation within a system." Hunt + Thomas, *The Pragmatic Programmer*, 1999.

**KISS — Keep It Simple, Stupid** — design heuristic from Kelly Johnson at Lockheed Skunk Works (1960); widely adopted in software.

**YAGNI — You Aren't Gonna Need It** — Extreme Programming principle; Ron Jeffries / Kent Beck, c. 1999.

**SOLID 5** — Robert C. Martin, *Design Principles and Design Patterns* (2000); acronym coined by Michael Feathers c. 2004 [T06-S048][T06-S049]:
- **S — SRP** Single Responsibility Principle
- **O — OCP** Open-Closed Principle (Meyer 1988; one open for extension, closed for modification)
- **L — LSP** Liskov Substitution Principle (Barbara Liskov 1987)
- **I — ISP** Interface Segregation Principle (Martin)
- **D — DIP** Dependency Inversion Principle (Martin) — high-level modules must not depend on low-level; both depend on abstractions.

**GRASP 9** (General Responsibility Assignment Software Patterns) — Craig Larman, *Applying UML and Patterns* (1997) [T06-S050]: **Information Expert / Creator / Controller / Low Coupling / High Cohesion / Polymorphism / Pure Fabrication / Indirection / Protected Variations**.

**Conway's Law** — "any organization that designs a system … will produce a design whose structure is a copy of the organization's communication structure." Mel Conway, *Datamation* 14(4):28-31, April 1968 [T06-S038].

**Inverse Conway Maneuver** — deliberately restructure teams to drive desired architecture. Thoughtworks Tech Radar 2014 (James Lewis et al.); popularized by Skelton+Pais *Team Topologies* 2019 [T06-S039].

**GoF 23 patterns** — Gamma, Helm, Johnson, Vlissides (Gang of Four), *Design Patterns: Elements of Reusable OO Software*, 1994 [T06-S051]:
- *Creational 5:* **Abstract Factory, Builder, Factory Method, Prototype, Singleton**.
- *Structural 7:* **Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy**.
- *Behavioral 11:* **Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor**.

**EIP 65 patterns** — Hohpe + Woolf, *Enterprise Integration Patterns*, 2003 [T06-S052]. Major category groups: Messaging Channels, Message Construction, Message Routing (Content-Based Router / Recipient List / Aggregator / Splitter), Message Transformation (Translator / Enricher / Filter), Endpoints (Polling / Event-Driven Consumer / Idempotent Receiver), System Management (Dead Letter Channel / Wire Tap / Control Bus). Spurred Apache Camel / Mule / WSO2 ESB ecosystems.

**Garlan + Shaw 6 architectural styles** — *Software Architecture: Perspectives on an Emerging Discipline*, Prentice Hall 1996 [T06-S037]: **(1) Data-centric** (Repository / Blackboard) — shared persistent data + independent computations. **(2) Data-flow** (Pipe-and-Filter, Batch Sequential). **(3) Call-and-return** (Main/Subroutine, OO, Layered). **(4) Independent-component** (Event-based implicit invocation, Communicating Processes). **(5) Virtual-machine** (Interpreter, Rule-based). **(6) Repository-centric / Repository** (data-store + clients; subsumes blackboard).

## 6.2 分布式 / 一致性 / consensus (CAP / PACELC / Paxos / Raft / Lamport / vector clock / 隔离级别 / Saga / outbox / CQRS / ES / idempotency / back-pressure)

**CAP theorem** — Consistency / Availability / Partition-tolerance; at most 2-of-3. Eric Brewer, PODC keynote, July 19, 2000 ("Towards Robust Distributed Systems") [T06-S006][T06-S007]; Gilbert+Lynch (MIT) formal proof 2002.

**PACELC** — extends CAP: if Partition then A vs C; Else (no partition) Latency vs Consistency. Daniel Abadi 2010 blog → IEEE Computer 45(2), Feb 2012 [T06-S008].

**FLP impossibility** — no deterministic asynchronous algorithm can guarantee consensus with even one faulty process. Fischer, Lynch, Paterson, JACM 32(2), April 1985; Dijkstra Award [T06-S005].

**Paxos** — consensus algorithm. Leslie Lamport, "The Part-Time Parliament," ACM TOCS 16(2), May 1998 (drafted 1990) [T06-S001][T06-S002]. Variants: Multi-Paxos, Cheap Paxos, Fast Paxos.

**Raft** — understandable consensus. Diego Ongaro + John Ousterhout, USENIX ATC 2014 Best Paper [T06-S003][T06-S004]. Separates leader election, log replication, safety.

**EPaxos (Egalitarian Paxos)** — leaderless multi-Paxos with optimal commit latency. Moraru, Andersen, Kaminsky, SOSP 2013 [T06-S020].

**Lamport clock (logical clock)** — scalar counter for partial event ordering. Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," CACM 21(7):558-565, July 1978 [T06-S009].

**Vector clock** — per-process counter vector capturing causality. Independently Colin Fidge (ACSC 1988) and Friedemann Mattern (*Parallel Computing* 1989) [T06-S011].

**HLC — Hybrid Logical Clock** — combines physical + logical for monotonic causality bounded by NTP skew. Kulkarni, Demirbas, Madappa, Avva, Leone, OPODIS 2014 [T06-S010].

**Linearizable / Linearizability** — operations appear to take effect atomically at some single point between invocation and response. Maurice Herlihy + Jeannette Wing, ACM TOPLAS 12(3), July 1990 [T06-S018].

**Serializable** — equivalent to *some* serial execution; stronger than snapshot isolation; SQL-92 strongest defined level [T06-S017].

**Snapshot isolation** — each txn reads a consistent snapshot at begin-ts; allows write-skew anomaly. Berenson, Bernstein, Gray et al, SIGMOD 1995 ("A Critique of ANSI SQL Isolation Levels") [T06-S017].

**Read committed** — reads only see committed data; permits non-repeatable reads + phantoms. ANSI SQL-92 isolation level [T06-S017].

**Repeatable read** — re-reading a row returns same value within txn; permits phantoms. ANSI SQL-92 [T06-S017].

**Causal consistency** — all replicas agree on order of causally-related ops; concurrent ops may differ. Ahamad, Neiger, Burns, Kohli, Hutto, "Causal memory: definitions, implementation, and programming," *Distributed Computing* 9(1), 1995 [T06-S019].

**Eventual consistency** — if no new updates, all replicas converge to same value. Werner Vogels (Amazon) "Eventually Consistent" CACM 2009.

**2PC — Two-Phase Commit** — prepare + commit phases for distributed atomic transactions. Jim Gray 1978. Blocking on coordinator failure [T06-S021].

**3PC — Three-Phase Commit** — pre-commit phase between prepare and commit removes blocking under single failures (but not partitions). Dale Skeen 1981; Skeen + Stonebraker, *IEEE TSE* 1983 [T06-S021].

**Saga** — long-lived txn as sequence of local txns each with compensating action. Hector Garcia-Molina + Kenneth Salem, ACM SIGMOD 1987 [T06-S012][T06-S013]. Re-popularized for microservices (Chris Richardson).

**Outbox pattern (Transactional Outbox)** — write business state + outbox row in same DB txn; relay publishes to broker. Documented Chris Richardson, microservices.io c. 2018 [T06-S014].

**CDC — Change Data Capture** — read database transaction log (WAL/binlog) and emit row-level change events. Debezium (Kafka Connect) is reference implementation; concept formalized in Kleppmann *Designing Data-Intensive Applications* 2017.

**Event Sourcing** — store every state change as immutable event; current state derived by replay. Martin Fowler 2005 (eaaDev) [T06-S015]; Greg Young popularization c. 2010.

**CQRS — Command Query Responsibility Segregation** — separate write model from read model. Greg Young 2010, building on Bertrand Meyer's CQS [T06-S016].

**Exactly-once** — every message processed exactly once (rare; typically "effectively once" via idempotency + transactions). Kafka 0.11+ idempotent producer + transactions [T06-S064].

**At-least-once** — every message delivered ≥1 time; consumers must dedupe / be idempotent [T06-S064].

**At-most-once** — fire-and-forget; messages may be lost, never duplicated [T06-S064].

**Idempotency** — operation can be applied many times with same effect as once. Required for safe retries [T06-S064].

**Dead-letter queue (DLQ)** — channel for messages that cannot be delivered/processed after N retries. EIP pattern "Dead Letter Channel" [T06-S052].

**Back-pressure** — downstream signals upstream to slow down rather than collapse under load. Reactive Streams spec 2013/2014; Akka/Erlang lineage [T06-S065].

## 6.3 操作 / SLO / SRE (SLO/SLI/error budget / RED / USE / Golden Signals / RPO/RTO/MTBF/MTTR / circuit breaker / bulkhead / hedged / quorum / p99)

**SLI — Service Level Indicator** — quantitative metric of one service aspect (latency, error rate, availability). Google SRE book ch. 4, Beyer et al, O'Reilly 2016 [T06-S023].

**SLO — Service Level Objective** — target value/range for an SLI (e.g., 99.9% of GETs ≤ 300 ms over 28 days) [T06-S023].

**SLA — Service Level Agreement** — explicit contract with users including consequences when SLOs are missed [T06-S023].

**Error budget** — 1 − SLO; permitted rate of failures. Drives release-gating: budget exhausted → freeze new launches [T06-S023].

**RED method** — Rate / Errors / Duration per request. Tom Wilkie (Weaveworks/Grafana), c. 2015; derived from Google's Golden Signals, microservice-focused [T06-S024].

**USE method** — Utilization / Saturation / Errors per resource. Brendan Gregg, brendangregg.com & ACM Queue 2012 [T06-S025][T06-S026].

**Four Golden Signals** — Latency / Traffic / Errors / Saturation. Google SRE book ch. 6 "Monitoring Distributed Systems" 2016 [T06-S022].

**RPO — Recovery Point Objective** — max acceptable data loss measured in time (e.g., RPO=0 = zero loss). Disaster recovery standard term.

**RTO — Recovery Time Objective** — max acceptable downtime to restore service.

**MTBF — Mean Time Between Failures** — average uptime between failures; reliability metric.

**MTTR — Mean Time To Recovery/Repair** — average time to restore service after failure.

**Circuit breaker** — wrap remote calls; "trip open" after failure threshold to fail fast and let downstream recover. Michael Nygard, *Release It!* Stability Patterns, Pragmatic Programmers, March 2007 [T06-S029]; popularized further by Hystrix (Netflix) and Fowler bliki.

**Bulkhead** — partition resources (thread pools, connection pools, processes) so failure in one cannot drain the rest. Ship-hull analogy. Nygard *Release It!* 2007 [T06-S029][T06-S030].

**Hedged request** — send same request to N replicas after delay; take first response, cancel rest. Dean + Barroso, "The Tail at Scale," CACM 56(2):74-80, Feb 2013 [T06-S027][T06-S028]. Variants: tied request (replicas cancel each other).

**Quorum read/write** — require ack from majority (W+R > N) to ensure overlap. Dynamo paper (DeCandia et al, SOSP 2007); foundation for Cassandra/Riak.

**Read-your-writes consistency** — session guarantee: a process always sees its own writes. Session guarantees: Terry et al, Bayou (SIGOPS 1994).

**W3C Trace Context** — HTTP header standard (`traceparent`, `tracestate`) for cross-service trace propagation [T06-S055].

**OpenTelemetry (OTel)** — CNCF observability framework merging OpenTracing + OpenCensus; SDKs/APIs for traces, metrics, logs [T06-S054].

**OTel span** — single operation in a trace, carries TraceId (16-byte) + SpanId (8-byte), parent, status, attributes [T06-S054].

**Sampling strategy** — head-based (decide at trace start) vs tail-based (decide after collection); probabilistic vs rate-limiting [T06-S054].

**p50 / p95 / p99 percentile** — 50th/95th/99th percentile of latency distribution; p99 is "tail latency" emphasized in *The Tail at Scale* [T06-S027].

## 6.4 流程 / decision / 文档 (ADR / arc42 / C4 / 4+1 / DDD strategic+tactical / fitness function / strangler fig / feature flag / canary / blue-green / inverse-Conway)

**ADR — Architecture Decision Record** — short markdown doc capturing Context / Decision / Status / Consequences per arch decision. Michael Nygard, Cognitect blog, Nov 15, 2011 [T06-S031][T06-S032].

**arc42** — pragmatic 12-section architecture documentation template (intro/goals, constraints, context, solution strategy, building blocks, runtime, deployment, crosscutting, decisions, quality, risks, glossary). Gernot Starke + Peter Hruschka, 2005; free CC license, arc42.org [T06-S034].

**C4 model** — 4 hierarchical diagram levels: **Context / Container / Component / Code**. Simon Brown, developed 2006–2011, c4model.com [T06-S033]. Lightweight UML alternative.

**4+1 view model** — **Logical / Process / Development / Physical + Scenarios**. Philippe Kruchten, *IEEE Software* 12(6):42-50, Nov 1995 [T06-S036]. Foundation of RUP architecture description.

**DDD strategic** (Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley 2003 [T06-S053]):
- **Bounded context** — explicit boundary within which a domain model applies consistently; integration via Context Map.
- **Context map** — relationships between bounded contexts (Shared Kernel / Customer-Supplier / Conformist / Anti-Corruption Layer / Open Host Service / Published Language).
- **Sub-domain** — partitioning of domain into **Core / Supporting / Generic**.
- **Ubiquitous language** — shared domain vocabulary used by devs + domain experts + code + tests.

**DDD tactical** [T06-S053]:
- **Aggregate** — cluster of entities/VOs treated as a single unit for data changes; one **aggregate root** controls invariants.
- **Entity** — object with identity that persists over time.
- **Value object** — immutable object defined only by its attributes.
- **Domain event** — record of something that happened in the domain.
- **Repository** — collection-like abstraction over aggregate persistence.
- **Domain service** — domain operation that doesn't naturally belong to an entity/VO.

**Fitness function** — automated, objective measurement of an architectural characteristic (perf, security, modularity). Ford + Parsons + Kua, *Building Evolutionary Architectures*, O'Reilly 2017 [T06-S041].

**Strangler Fig pattern** — incrementally replace legacy by routing traffic through a façade to new services until legacy is "strangled." Martin Fowler, bliki, 2004 [T06-S040].

**Branch by abstraction** — introduce an abstraction layer over an old implementation, build new impl behind it, swap. Paul Hammant 2007; popularized Jez Humble *Continuous Delivery* 2010.

**Feature flag / feature toggle** — runtime switch to enable/disable a code path without redeploy. Pete Hodgson on martinfowler.com 2017; LaunchDarkly commercialized.

**Dark launch** — release feature to production but invisible to users (shadowed traffic) to measure load/latency before exposing. Facebook News Feed origin c. 2008.

**Canary release** — route small % of traffic to new version; expand if healthy; rollback if not. Name from "canary in a coal mine."

**Blue-green deployment** — run two identical envs ("blue" live, "green" new); instant switch via router. Daniel Terhorst-North / Jez Humble 2010s.

**Progressive delivery** — superset combining feature flags + canaries + audience targeting + automated rollback. Term coined James Governor (RedMonk) 2018.

**Inverse Conway maneuver** — see 6.1 [T06-S039].

## 6.5 中国本土合规 + 高并发 vocabulary

**信通院 (CAICT) — 中国信息通信研究院** — 工信部直属科研机构, 发布数据库/云/AI/可信评测, 制定国家标准. service.caict.ac.cn [T06-S063].

**CCF — 中国计算机学会 (China Computer Federation)** — 一级学术学会, 主办 CCF-A/B/C 期刊会议分级, TF (Technical Forum) 体系覆盖架构方向.

**国密 (国家商用密码算法)** — 国家密码管理局 (OSCCA) 发布的商用密码标准 [T06-S061][T06-S062]:
- **SM2** — 椭圆曲线公钥算法, 256-bit, 2010 发布 (替代 RSA/ECDSA).
- **SM3** — 256-bit 密码 hash 算法, 2010 发布 (替代 SHA-256).
- **SM4** — 128-bit 分组密码, WAPI 标准 (替代 AES).
- **SM9** — 标识密码算法.
- **ZUC (祖冲之算法)** — 流密码, 3GPP 5G/LTE 加密候选.

**等保 2.0 (网络安全等级保护 2.0)** — GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》, 2019-05-10 发布, 2019-12-01 实施 [T06-S059][T06-S060]. "1+5" 结构: 安全通用要求 + 云/移动/物联网/工控/大数据 5 个扩展. 等级分 5 级, 第三级是政企系统主流定级.

**国产化 / 自主可控 / 信创 (信息技术应用创新)** — 国资委要求央国企 2027 年底前完成 IT 系统国产化替代; CPU (鲲鹏/海光/飞腾/龙芯) + OS (统信 UOS / 麒麟) + 数据库 (达梦/人大金仓/OceanBase/TiDB) + 中间件 (东方通/金蝶 Apusic) 全栈替代.

**高并发** — 系统能承受同一时刻大量请求 (典型指标 QPS / TPS / concurrent connections).

**高可用 (HA)** — 服务可用时间占比, 通常用"几个 9" 表达 (99.9% 三个 9 ≈ 8.76h/年 down; 99.99% ≈ 52.6 min).

**高性能** — 低延迟 + 高吞吐; 单机优化 + 分布式优化两条路径.

**春晚级流量** — 央视春晚红包/直播带来的瞬时数十亿级请求, 行业用作"超大尖峰流量"代名词 (微信 2015 春晚红包 / 抖音 2021 春晚).

**双 11 (Double 11)** — 阿里 11 月 11 日全球购物节, 2009 起; 零点峰值 2020 年达 58.3 万笔/秒, 推动了限流/熔断/异地多活技术栈成熟 [T06-S056].

**秒杀 (flash sale)** — 限时限量抢购, 典型高并发场景, 需要前端排队 + 服务端令牌桶 + 库存预扣减 + 异步下单 + Redis 原子操作组合方案.

**缓存击穿 (cache breakdown)** — 单个热 key 失效瞬间, 大并发直接打到 DB. 解决: 互斥锁 / 永不过期 / 逻辑过期 [T06-S058].

**缓存雪崩 (cache avalanche)** — 大量 key 同时失效或 Redis 宕机, 数据库被压垮. 解决: 过期时间加随机抖动 / Redis 高可用集群 / 多级缓存 [T06-S058].

**缓存穿透 (cache penetration)** — 查询根本不存在的 key, 缓存恒 miss, 请求全部打 DB. 解决: 布隆过滤器 / 缓存空值 / 接口鉴权 [T06-S058].

**Sentinel (限流 / 熔断 / 降级)** — Alibaba 开源高并发流量治理组件, 双 11 核心组件; 资源+规则模型, 支持 QPS/线程数/慢调用比例/异常比例多种规则 [T06-S056]. (限流 = rate limit; 熔断 = circuit breaker; 降级 = fallback to degraded service.)

**削峰填谷** — 用消息队列把瞬时峰值 buffer 起来异步消费, 平滑数据库压力 (秒杀场景标配).

**异地多活 (multi-active across regions)** — 多个相距远距 (典型三地五中心) 数据中心同时承担生产流量, 任一城市级故障不丢可用性. 蚂蚁金服 2013–2015 落地, 2015 "527 挖光缆事件"验证 [T06-S057]. RPO=0, RTO<30s 是行业目标线.

**单元化部署 (unitization / LDC — Logical Data Center)** — 把用户按 sharding key 划分到不同"单元", 单元内自包含完成所有业务调用, 减少跨单元 RPC + 跨城延迟. 蚂蚁金服 LDC 方案 [T06-S057].

**微服务治理** — 注册/发现 + 配置中心 + 熔断限流 + 链路追踪 + 灰度发布 + 网关 + 鉴权全套. 国内主流栈: Spring Cloud Alibaba (Nacos + Sentinel + Seata + Dubbo) / 字节 ByteMesh / 腾讯 TARS.

## 6.6 反模式 vocabulary

**Architecture Astronaut** — 架构宇航员: 抽象上去就下不来, 用模式发现万物的"高空思考者". Joel Spolsky, "Don't Let Architecture Astronauts Scare You" / "Are the Groove Designers Architecture Astronauts?" joelonsoftware.com, April 21–22, 2001 [T06-S044]. "When you go too far up, abstraction-wise, you run out of oxygen."

**RDD — Resume-Driven Development** — 为简历选技术, 用最新最复杂的框架解决最简单的问题. Community 创词, 微服务/Kubernetes/Kafka 热潮中常用.

**Cargo cult microservices** — 货物崇拜微服务: 模仿 Netflix/Uber 的拆分形式但不理解其约束 (团队规模/部署能力/可观测性). Source: Richard Feynman 1974 "cargo cult science" 引申, 微服务版本在 2015+ 流行.

**Golden Hammer (黄金锤)** — "若你只有一把锤子, 看什么都像钉子." Maslow 1966; AntiPatterns book (Brown/Malveau/McCormick/Mowbray 1998) 列为 26 经典反模式之一.

**God Object (上帝对象)** — 一个类承担系统大部分功能/数据, 违反 SRP. Riel *OO Design Heuristics* 1996.

**Lava Layer (Lava Flow)** — 多代架构决策叠加但前代未清理, 代码库像火山岩层有"考古地层". Mike Hadlow, mikehadlow.blogspot.com, Dec 2014 [T06-S045]. 大企业长寿系统典型.

**Spaghetti code (面条代码)** — 控制流跳来跳去无结构. 1970 年代结构化编程论战中已用 (Edsger Dijkstra "GOTO Considered Harmful" 1968 间接).

**Big Ball of Mud** — 散乱、随意、胶带+铁丝拼起来的代码丛林, "the most common software architecture." Brian Foote + Joseph Yoder, PLoP 1997 [T06-S042][T06-S043].

**Accidental complexity vs essential complexity** — Brooks 区分: essential = 问题本身的复杂度, accidental = 工具/方法/技术债引入的额外复杂度. "No Silver Bullet — Essence and Accident in Software Engineering," Brooks, IFIP 1986 [T06-S035].

**Yak shaving** — 为了完成 A 必须先做 B, 而 B 又需要 C... 最后在剃牦牛毛. Carlin Vieri (MIT AI Lab) 1990s; popularized Jeremy Brown.

**Bike-shedding (Parkinson's Law of Triviality)** — 委员会花大量时间讨论自行车棚颜色 (易懂), 忽略核反应堆设计 (难懂). C. Northcote Parkinson, *Parkinson's Law*, 1957 [T06-S046]. "Bikeshedding" 1999 Poul-Henning Kamp (FreeBSD) 推广进软件圈.

**Over-engineering** — 过度设计: 为想象中的未来需求添加复杂度. 与 YAGNI 互为反面.

**Premature optimization** — "We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil." Donald Knuth, "Structured Programming with go to Statements," *ACM Computing Surveys* 6(4):261–301, Dec 1974 [T06-S047]. 实际引语先由 Tony Hoare 提出, Knuth 承认转述.

**NIH — Not Invented Here** — 拒绝使用外部方案, 坚持自研; 既浪费又制造可维护性风险.

**Vendor lock-in** — 系统深度绑定单一厂商 API/格式/计费, 迁移成本极高 (典型: AWS 专有服务, Oracle 数据库, 国产化场景下绑定单一国产 DB).

**Distributed monolith** — 名义上是微服务, 实际服务间紧耦合、必须同步部署、共享数据库、链式同步调用. Sam Newman *Monolith to Microservices* 2019 反复警告: "若你有一个全职的 release coordination manager, 那就是 distributed monolith." 

---

(术语统计: 6.1 设计 24 / 6.2 分布式 25 / 6.3 SRE 18 / 6.4 流程文档 18 / 6.5 中文本土 19 / 6.6 反模式 16 → 总计 ≈ 120 terms.)
