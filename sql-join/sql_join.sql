SELECT t.id, t.location, t.fault_severity, e.event_type, st.severity_type, r.resource_type, l.log_feature, l.volume
FROM train as t
LEFT OUTER JOIN severity_type AS st
ON t.id = st.id
LEFT OUTER JOIN event_type AS e
ON t.id = e.id
LEFT OUTER JOIN resource_type AS r
ON t.id = r.id
LEFT OUTER JOIN log_feature AS l
ON t.id = l.id;