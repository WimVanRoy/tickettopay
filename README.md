# Ticket to pay for NMBS

## Structure output:

```py
data = [
	{
	    "date": "03/01/2019",  # Reisdatum
	    "ticket_type": "Treinkaart",  # Ticket type
	    "ticket_number": "123456...",
	    "ticket_last_usage": "11/07/2019",
	    "departure_station": "ZEDELGEM",
	    "destination_station": "BRUSSEL-CENTRAAL",
	    "stop_station: "BRUGGE",
	    "planned_time_dep": "11:00",
	    "planned_time_arr": "11:30",
	    "planned_train_no": ["0513", "0444"],
	    "real_time_dep": "11:00",
	    "real_time_arr": "11:50",
	    "real_train_no": ["0513", "0444"],
	    "delay": 1200,
	}
]

# Fetch data from:

https://opendata.infrabel.be/pages/home/

`https://opendata.infrabel.be/explore/dataset/ruwe-gegevens-van-stiptheid-d-1/api/?disjunctive.train_no&disjunctive.relation&disjunctive.train_serv&disjunctive.line_no_dep&disjunctive.relation_direction&disjunctive.ptcar_lg_nm_nl&disjunctive.line_no_arr&sort=planned_date_dep&rows=-1&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoiZGVsYXlfYXJyIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzBEOUZGRiJ9XSwieEF4aXMiOiJyZWFsX2RhdGVfZGVwIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InJ1d2UtZ2VnZXZlbnMtdmFuLXN0aXB0aGVpZC1kLTEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnRyYWluX25vIjp0cnVlLCJkaXNqdW5jdGl2ZS5yZWxhdGlvbiI6dHJ1ZSwiZGlzanVuY3RpdmUudHJhaW5fc2VydiI6dHJ1ZSwiZGlzanVuY3RpdmUubGluZV9ub19kZXAiOnRydWUsImRpc2p1bmN0aXZlLnJlbGF0aW9uX2RpcmVjdGlvbiI6dHJ1ZSwiZGlzanVuY3RpdmUucHRjYXJfbGdfbm1fbmwiOnRydWUsImRpc2p1bmN0aXZlLmxpbmVfbm9fYXJyIjp0cnVlLCJzb3J0IjoicGxhbm5lZF9kYXRlX2RlcCJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D``
