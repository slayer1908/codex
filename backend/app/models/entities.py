from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    website_url = Column(String(1024), nullable=False)
    campaign_name = Column(String(255), nullable=False)
    status = Column(String(50), default="draft")
    budget = Column(Float, nullable=False)
    currency = Column(String(8), default="USD")
    bidding_strategy = Column(String(100), default="maximize_conversions")
    campaign_metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    keywords = relationship("Keyword", back_populates="campaign")
    ads = relationship("Ad", back_populates="campaign")
    metrics = relationship("PerformanceMetric", back_populates="campaign")


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    term = Column(String(255), nullable=False)
    match_type = Column(String(25), nullable=False)
    intent = Column(String(50), default="commercial")
    score = Column(Float, default=0.0)

    campaign = relationship("Campaign", back_populates="keywords")


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    ad_type = Column(String(50), nullable=False)
    headline = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    assets = Column(JSON, default={})

    campaign = relationship("Campaign", back_populates="ads")


class PerformanceMetric(Base):
    __tablename__ = "performance_metrics"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
    spend = Column(Float, default=0.0)
    ctr = Column(Float, default=0.0)
    conversion_rate = Column(Float, default=0.0)

    campaign = relationship("Campaign", back_populates="metrics")


class SearchTerm(Base):
    __tablename__ = "search_terms"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    query = Column(String(255), nullable=False)
    clicks = Column(Integer, default=0)
    conversions = Column(Integer, default=0)


class AudienceBehavior(Base):
    __tablename__ = "audience_behavior"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    audience_segment = Column(String(255), nullable=False)
    behavior = Column(JSON, default={})


class ConversionEvent(Base):
    __tablename__ = "conversion_events"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    event_name = Column(String(255), nullable=False)
    value = Column(Float, default=0.0)
    occurred_at = Column(DateTime, default=datetime.utcnow)
