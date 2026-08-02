# ADR 0001 - Maintenance cycle data model

**Status:** Accepted
**Date:** 31/07/2026

## Context
-There's no local standard to categorize criticality of medical equipment.
-There's no control over detecting and reporting and issue by the system.
-How to solve the relation between an equipment and its maintenance?

## Decision
Since there's no local standard to categorize criticality of medical equipment, it is established that the engineer assigns this field by their own judgement.

Downtime is measured by the first report of an issue; each equipment can have more than one open maintenance at a time; and the equipment-maintenance relationship is established by a One-to-Many (1:N).

Additionally, a priority field is introduced at the maintenance level independent from equipment criticality -criticality reflects how severe a failure would be in general, while priority reflects how urgent a specific intervention is right now.

## Consequences
-Since the 1:N relation is already explicitly represented, (equipo_id as a reference) the model is ready for an SQL-migration without redesign.
-The business logic must display, per equipment, the list of active maintenance tasks sorted by priority, since multiple maintenance tasks can coexist.
-Metrics (downtime, operational availability, expired maintenances) are calculated from these fields; they are not directly stored.