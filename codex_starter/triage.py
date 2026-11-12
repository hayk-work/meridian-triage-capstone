"""Deterministic recommendations requiring human review."""
import math


def prioritize(ticket):
    """Validate structured fields without modifying the input."""
    if not isinstance(ticket.get('id'), str) or not ticket['id'].strip():
        raise ValueError('id must be a nonblank string')
    for field, allowed in [('category', ('incident', 'access', 'question')),
                           ('impact', ('single', 'team', 'company'))]:
        if ticket.get(field) not in allowed:
            raise ValueError(f'invalid {field}')
    if not isinstance(ticket.get('blocked'), bool):
        raise ValueError('blocked must be a Boolean')
    age = ticket.get('age_hours')
    if (isinstance(age, bool) or not isinstance(age, (int, float))
            or age < 0 or (isinstance(age, float) and not math.isfinite(age))):
        raise ValueError('age_hours must be a finite, nonnegative number')
    manual = ticket.get('manual_priority')
    if manual not in (None, 'P1', 'P2', 'P3'):
        raise ValueError('invalid manual_priority')
    if manual is not None:
        priority, rule, reason = manual, 'manual', 'Valid manual priority retained.'
    elif ticket['category'] == 'incident' and ticket['impact'] == 'company' and ticket['blocked']:
        priority, rule, reason = 'P1', 'company_outage', 'Incident blocks the whole company.'
    elif ticket['blocked']:
        priority, rule, reason = 'P2', 'blocked', 'Ticket blocks work.'
    elif age >= 24:
        priority, rule, reason = 'P2', 'aging', 'Ticket is at least 24 hours old.'
    else:
        priority, rule, reason = 'P3', 'standard', 'No manual, outage, blocked or aging rule applies.'
    return dict(id=ticket['id'], priority=priority, rule=rule,
                reason=reason, review_required=True)
